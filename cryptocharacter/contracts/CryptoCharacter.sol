event
available metamask account
Default
Crypto Characters
Explorer
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
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
4 of 7
Output
Using Solidity compiler version 0.5.10
Success in compilation
External account detected. Opening external account provider...
Got receipt: 0x98513338def0fba55f5a577f2d09eb2232f6d573b4bb84f1f3fac0fa26fbbce2
Transaction mined, verifying code...
Contract deployed at address 0x217e76b42076c92da05779493297834723a77b38.
Done.
Using Solidity compiler version 0.5.10
Success in compilation
Using Solidity compiler version 0.5.10
Success in compilation
Contract on chain is different, redeploying.
External account detected. Opening external account provider...
Got receipt: 0x1011f344d313ec3e0663a09694ed3924a64c4134bfe618aaf452ac29d85b3873
Transaction mined, verifying code...
Contract deployed at address 0xc0c029583fa5201784c0398ca36f388ddf0b09b8.
Done.
Using Solidity compiler version 0.5.10
/contracts/CryptoCharacter.sol:102:17: TypeError: Wrong argument count for struct constructor: 1 arguments given but expected 2.
Event(
^ (Relevant source part starts here and spans across multiple lines).
[ERROR] Ate bad code and died, compilation aborted.
Using Solidity compiler version 0.5.10
Success in compilation
Contract on chain is different, redeploying.
External account detected. Opening external account provider...
Got receipt: 0xb0f43baf23d4119acc094d11826fc4f348564cd17cf058f88762ef20de192726
Transaction mined, verifying code...
Contract deployed at address 0x153459b0041c522e142274674537a266ae4975c8.
Done.
Using Solidity compiler version 0.5.10
Success in compilation
Contract on chain is the same, not redeploying.
Done.
Using Solidity compiler version 0.5.10
Success in compilation
Contract on chain is different, redeploying.
External account detected. Opening external account provider...
Got receipt: 0xd9aff30dc148a7a8183f92bdc77c84de2da87204a9b8341552295cd34d5b6c89
Transaction mined, verifying code...
Contract deployed at address 0xba2d93afed2832ef19368aed31bf8c09a53a7219.
Done.
Powered bySuperblocks
Account balance: 0Gas Limit: 7900000Gas Price: 1 Gweihttp://51.105.171.12:8545
push, accepted
