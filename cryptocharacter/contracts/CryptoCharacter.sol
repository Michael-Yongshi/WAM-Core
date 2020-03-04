// metamask network vincent: http://51.105.171.12
pragma solidity ^0.5.10;

import "../node_modules/openzeppelin-solidity/contracts/token/ERC721/IERC721.sol";
import "../node_modules/openzeppelin-solidity/contracts/token/ERC721/IERC721Receiver.sol";
import "../node_modules/openzeppelin-solidity/contracts/introspection/ERC165.sol";
import "../node_modules/openzeppelin-solidity/contracts/math/SafeMath.sol";

contract CryptoCharacter is IERC721, ERC165 {

    // Use Open Zeppelin's SafeMath library to perform arithmetic operations safely.
    using SafeMath for uint256;

    /*
        A Character has only 5 parts that can change according to its DNA.
        When we generate DNA, we get a 10 digit long number, and each pair corresponds to a specific ingredient.

        E.g. DNA 5142446803 - 51_Basis/42_Cheeses/44_Meats/68_Spices/03_Vegetables
    */
    uint constant dnaDigits = 10;
    uint constant dnaModulus = 10 ** dnaDigits;

    // Equals to `bytes4(keccak256("onERC721Received(address,address,uint256,bytes)"))`
    // which can be also obtained as `IERC721Receiver(0).onERC721Received.selector`
    bytes4 private constant _ERC721_RECEIVED = 0x150b7a02;

    struct Character {
        string identifier;
        string name;
        string unit;
        string race;
        uint dna;
    }

    Character[] public characters;

    struct Event {
        string description;
    }

    Event[] public events;
    // string[] public events;

    // Mapping from owner to id of Character
    mapping (uint => address) public characterToOwner;

    // Mapping from id of Character to id of Event
    mapping (uint => uint) public eventToCharacter;

    // Mapping from owner to number of owned token
    mapping (address => uint) public ownerCharacterCount;

    // Mapping from character to number of owned events
    mapping (uint => uint) public characterEventCount;

    // Mapping from token ID to approved address
    mapping (uint => address) characterApprovals;
// Mapping from owner to operator approvals
    mapping (address => mapping (address => bool)) private operatorApprovals;

    // Create random Character from string (name) and DNA
    function _createCharacter(
        string memory _identifier,
        string memory _name,
        string memory _unit,
        string memory _race,
        uint _dna
        )
        internal
        isUnique(_identifier, _dna)
    {
        // Add Character to array and get id
        uint id = SafeMath.sub(
            characters.push(
                Character(
                    _identifier,
                    _name,
                    _unit,
                    _race,
                    _dna
                    )
                ),
            1);
        // Map owner to id of Character
        assert(characterToOwner[id] == address(0));
        characterToOwner[id] = msg.sender;
        ownerCharacterCount[msg.sender] = SafeMath.add(ownerCharacterCount[msg.sender], 1);
    
        // Add creation event to character
        // string memory comment = "Character Created";
        // createEvent(
        //     id,
        //     comment
        //     );
    }

    // Create Event from string
    function createEvent(
        uint _characterId,
        string memory _description
        )
        public
    {
        // Add event to array and get id
        uint id = SafeMath.sub(
            events.push(
                Event(
                    _description
                    )
                ),
            1);

        // Map id of Character to id of Event
        assert(eventToCharacter[id] == uint(0));
        eventToCharacter[id] = _characterId;
        characterEventCount[_characterId] = SafeMath.add(characterEventCount[_characterId], 1);
    }

    // Creates random Character from string (identifier)
    function createRandomCharacter(
        string memory _identifier,
        string memory _name,
        string memory _unit,
        string memory _race
        )
        public
    {
        uint randDna = generateRandomDna(_identifier, msg.sender);
        _createCharacter(
            _identifier,
            _name,
            _unit,
            _race,
            randDna
            );
    }

    // Generate random DNA from string (identifier) and address of the owner (creator)
    function generateRandomDna(string memory _str, address _owner)
        public
        pure
        returns(uint)
    {
        // Generate random uint from string (identifier) + address (owner)
        uint rand = uint(keccak256(abi.encodePacked(_str))) + uint(_owner);
        rand = rand % dnaModulus;
        return rand;
    }

    // Returns array of Characters found by owner
    function getCharactersByOwner(address _owner)
        public
        view
        returns(uint[] memory)
    {
        uint[] memory result = new uint[](ownerCharacterCount[_owner]);
        uint counter = 0;
        for (uint i = 0; i < characters.length; i++) {
            if (characterToOwner[i] == _owner) {
                result[counter] = i;
                counter++;
            }
        }
        return result;
    }

    // Returns array of Events found by characterId
    function getEventsByCharacter(uint256 _characterId)
        public
        view
        returns(uint[] memory)
    {
        uint[] memory result = new uint[](characterEventCount[_characterId]);
        uint counter = 0;
        for (uint i = 0; i < events.length; i++) {
            result[counter] = i;
            counter++;
        }
        return result;
    }

    // Transfer Character to other wallet (internal function)
    function transferFrom(address _from, address _to, uint256 _characterId)
        public
    {
        require(_from != address(0) && _to != address(0));
        require(_exists(_characterId));
        require(_from != _to);
        require(_isApprovedOrOwner(msg.sender, _characterId));
        ownerCharacterCount[_to] = SafeMath.add(ownerCharacterCount[_to], 1);
        ownerCharacterCount[_from] = SafeMath.sub(ownerCharacterCount[_from], 1);
        characterToOwner[_characterId] = _to;
        emit Transfer(_from, _to, _characterId);
        _clearApproval(_to, _characterId);
    }

    /**
     * Safely transfers the ownership of a given token ID to another address
     * If the target address is a contract, it must implement `onERC721Received`,
     * which is called upon a safe transfer, and return the magic value
     * `bytes4(keccak256("onERC721Received(address,address,uint256,bytes)"))`; otherwise,
     * the transfer is reverted.
    */
    function safeTransferFrom(address from, address to, uint256 characterId)
        public
    {
        // solium-disable-next-line arg-overflow
        this.safeTransferFrom(from, to, characterId, "");
    }

    /**
     * Safely transfers the ownership of a given token ID to another address
     * If the target address is a contract, it must implement `onERC721Received`,
     * which is called upon a safe transfer, and return the magic value
     * `bytes4(keccak256("onERC721Received(address,address,uint256,bytes)"))`; otherwise,
     */
    function safeTransferFrom(address from, address to, uint256 characterId, bytes memory _data)
        public
    {
        this.transferFrom(from, to, characterId);
        // solium-disable-next-line arg-overflow
        require(_checkOnERC721Received(from, to, characterId, _data));
    }

    /**
     * Internal function to invoke `onERC721Received` on a target address
     * The call is not executed if the target address is not a contract
     */
    function _checkOnERC721Received(address from, address to, uint256 characterId, bytes memory _data)
        internal
        returns(bool)
    {
        if (!isContract(to)) {
            return true;
        }

        bytes4 retval = IERC721Receiver(to).onERC721Received(msg.sender, from, characterId, _data);
        return (retval == _ERC721_RECEIVED);
    }

    // Burn Character - destroys Token completely
    function burn(uint256 _characterId)
        external
    {
        require(msg.sender != address(0));
        require(_exists(_characterId));
        require(_isApprovedOrOwner(msg.sender, _characterId));

        ownerCharacterCount[msg.sender] = SafeMath.sub(ownerCharacterCount[msg.sender], 1);
        characterToOwner[_characterId] = address(0);
    }

    // Returns count of Characters by address
    function balanceOf(address _owner)
        public
        view
        returns(uint256 _balance)
    {
        return ownerCharacterCount[_owner];
    }

    // Returns owner of the Character found by id
    function ownerOf(uint256 _characterId)
        public
        view
        returns(address _owner)
    {
        address owner = characterToOwner[_characterId];
        require(owner != address(0));
        return owner;
    }

    // Approve other wallet to transfer ownership of Character
    function approve(address _to, uint256 _characterId)
        public
    {
        require(msg.sender == characterToOwner[_characterId]);
        characterApprovals[_characterId] = _to;
        emit Approval(msg.sender, _to, _characterId);
    }

    // Return approved address for specific Character
    function getApproved(uint256 characterId)
        public
        view
        returns(address operator)
    {
        require(_exists(characterId));
        return characterApprovals[characterId];
    }

    /**
     * Private function to clear current approval of a given token ID
     * Reverts if the given address is not indeed the owner of the token
     */
    function _clearApproval(address owner, uint256 characterId) private {
        require(characterToOwner[characterId] == owner);
        require(_exists(characterId));
        if (characterApprovals[characterId] != address(0)) {
            characterApprovals[characterId] = address(0);
        }
    }

    /*
     * Sets or unsets the approval of a given operator
     * An operator is allowed to transfer all tokens of the sender on their behalf
     */
    function setApprovalForAll(address to, bool approved)
        public
    {
        require(to != msg.sender);
        operatorApprovals[msg.sender][to] = approved;
        emit ApprovalForAll(msg.sender, to, approved);
    }

    // Tells whether an operator is approved by a given owner
    function isApprovedForAll(address owner, address operator)
        public
        view
        returns(bool)
    {
        return operatorApprovals[owner][operator];
    }

    // Take ownership of Character - only for approved users
    function takeOwnership(uint256 _characterId)
        public
    {
        require(_isApprovedOrOwner(msg.sender, _characterId));
        address owner = this.ownerOf(_characterId);
        this.transferFrom(owner, msg.sender, _characterId);
    }

    // Check if Character exists
    function _exists(uint256 characterId)
        internal
        view
        returns(bool)
    {
        address owner = characterToOwner[characterId];
        return owner != address(0);
    }

    function _isApprovedOrOwner(address spender, uint256 characterId)
        internal
        view
        returns(bool)
    {
        address owner = characterToOwner[characterId];
        // Disable solium check because of
        // https://github.com/duaraghav8/Solium/issues/175
        // solium-disable-next-line operator-whitespace
        return (spender == owner || this.getApproved(characterId) == spender || this.isApprovedForAll(owner, spender));
    }

    // Check if Character is unique and doesn't exist yet
    modifier isUnique(string memory _identifier, uint256 _dna) {
        bool result = true;
        for(uint i = 0; i < characters.length; i++) {
            if(keccak256(abi.encodePacked(characters[i].identifier)) == keccak256(abi.encodePacked(_identifier)) && characters[i].dna == _dna) {
                result = false;
            }
        }
        require(result, "Character with name, unit and race combination already exists.");
        _;
    }

    // Returns whether the target address is a contract
    function isContract(address account)
        internal
        view
        returns(bool)
    {
        uint256 size;
        // XXX Currently there is no better way to check if there is a contract in an address
        // than to check the size of the code at that address.
        // See https://ethereum.stackexchange.com/a/14016/36603
        // for more details about how this works.
        // TODO Check this again before the Serenity release, because all addresses will be
        // contracts then.
        // solium-disable-next-line security/no-inline-assembly
        assembly { size := extcodesize(account) }
        return size > 0;
    }
}