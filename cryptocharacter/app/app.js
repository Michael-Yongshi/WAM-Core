// The object 'Contracts' will be injected here, which contains all data for all contracts, keyed on contract identifier:
// Contracts['CryptoCharacter'] = {
//  abi: [],
//  address: "0x..",
//  endpoint: "http://...."
// }

function Character(Contract) {
    this.web3 = null;
    this.instance = null;
    this.Contract = Contract;
}

if(typeof(Contracts) === "undefined") var Contracts={ CryptoCharacter: { abi: [] }};
var character = new Character(Contracts['CryptoCharacter']);

$(document).ready(function() {
    character.onReady();
});

Character.prototype.onReady = function() {
    this.init();
    this.bindInputs();
    this.loadInventory();
    showStatus("DApp loaded successfully.");
}
Character.prototype.initWeb3 = function(){
    // We create a new Web3 instance using either the Metamask provider
    // or an independent provider created towards the endpoint configured for the contract.
    if ((typeof window.ethereum !== 'undefined')
    || (typeof window.top.web3 !== 'undefined')) {
        console.log('injectedProvider');
        return new Web3(window['ethereum']|| window.top.web3.currentProvider)
    } else {
        // here you could use a different provider, maybe use an infura account, or maybe let the user know that they need to install metamask in order to continue
        return new Web3(new Web3.providers.HttpProvider(this.Contract.endpoint))
}
}
Character.prototype.init = function() {

    this.web3 = this.initWeb3();

    // Create the contract interface using the ABI provided in the configuration.
    this.instance = new this.web3.eth.Contract(this.Contract.abi,this.Contract.address,{from: window.top.web3.eth.accounts[0]});
    this.web3.eth.defaultAccount = window.top.web3.eth.accounts[0];
    console.log(this.instance)
}

Character.prototype.generateQrcode = function() {
    var typeNumber = 4;
    var errorCorrectionLevel = 'L';
    var qr = qrcode(typeNumber, errorCorrectionLevel);
    qr.addData( window.top.web3.eth.accounts[0]);
    qr.make();
    $("#qrcodec").html(qr.createImgTag());
}

// Generate random DNA from string
Character.prototype.getRandomDna = function(identifier, address, cb) {
    this.instance.methods.generateRandomDna(identifier, address).call().then(function(result){
         cb(result);
    }).catch(function(err){
        console.error('generateRandomDna ' + err )
    });
    

}

// Return all characters owned by specific address
Character.prototype.getCharactersByOwner = function(address, cb) {
    this.instance.methods.getCharactersByOwner(address).call().then(function(result){
         cb( result);
    }).catch(function(err){
        console.error('getCharactersByOwner ' + err  )
    });
}

// Waits for receipt from transaction
Character.prototype.waitForReceipt = function(hash, cb) {
    var that = this;

    // Checks for transaction receipt
    this.web3.eth.getTransactionReceipt(hash).then(function(receipt) {
   
        if (receipt !== null) {
            // Transaction went through
            if (cb) {
                cb(receipt);
            }
        } else {
            // Try again in 2 seconds
            window.setTimeout(function() {
                that.waitForReceipt(hash, cb);
            }, 2000);
        }
    }).catch(function(err){
        console.error('waitForReceipt ' + err  )
    });
    
   
}

// Create random Character from string (identifier)
Character.prototype.createRandomCharacter = function() {
    var that = this;

    // Get input values
    var name = $("#create-name").val();
    var unit = $("#create-unit").val();
    var race = $("#create-race").val();
    var identifier = name.concat(unit, race);

    // Validate identifier < 20 chars
    if(identifier.length > 20) {
        showStatus("Please identify your Character with less than 32 characters");
        return;
    }

    // Validate identifier > 0 chars
    if(!identifier) {
        showStatus("Please enter valid identifier");
        return;
    }

    $("#button-create").attr('disabled', true);


    this.instance.methods.createRandomCharacter(identifier, name, unit, race).send({from: window.top.web3.eth.accounts[0]}).then( function(txHash) {
                showStatus("Creating character");
                that.waitForReceipt(txHash.transactionHash, function(receipt) {
                    if(receipt.blockNumber > 0) {
                        showStatus("Creation successful");
                        $("#create-name").val("");
                        $("#create-unit").val("");
                        $("#create-race").val("");
                        // $("#create-tab .character-container .ingredients").html('');
                        $("#button-create").attr('disabled', false);
                        that.loadInventory();
                    }
                    else {
                        showStatus("Something went wrong, please try it again");
                        $("#button-create").attr('disabled', false);
                    }
                });
            }).catch(function(err){
                console.error('createRandomCharacter ' + err  )
                $("#button-create").attr('disabled', false);
            });
       
}

// Load all Characters owned by user
Character.prototype.loadInventory = function() {
    var that = this;
    this.instance.methods.getCharactersByOwner( window.top.web3.eth.accounts[0]).call().then(function( characterIds) {
                if(characterIds.length > 0) {
                    for(let i = 0; i < characterIds.length; i++) {
                         $(".inventory-list").html('');
                        that.instance.methods.characters(characterIds[i]).call().then( function(character) {
                            var realIndex = characterIds[i];
                            var characterName = character[0];
                            // var characterUnit = character[2];
                            // var characterRace = character[3];
                            var characterId = character[1];
                            var character = that.generateCharacterImage(character[1]);
                            var actionButtons = '<div class="action-buttons">\
                            \<button class="btn button-gift" id="'+realIndex+'">Transfer</button>\
                            \<button class="btn button-eat" id="'+realIndex+'">KIA</button>\
                            </div>';

                            $(".inventory-list").append('<div id="character-'+realIndex+'" class="col-lg-6">\
                            \<div class="character-container">\
                            \<p><span style="float: left;">'+characterName+'</span><span id="'+characterId+'" class="characterDna" style="float: right;">#'+characterId+'</span></p>\
                            \<div class="character-inner-container">\
                            <div class="ingredients">\
                            '+character+'\
                            </div></div>'+actionButtons+'</div></div>');

                            $(".inventory-list").append('</div>');
                            $(".inventory-list").append('</div>');
                            realIndex++;
                        }).catch(function(err){
                            console.error('characters ' + err  )
                        })
                    }
                }
                else {
                    $(".inventory-list").append('<p style="text-align: center; width: 100%">It seems you don\'t have any CryptoCharacter yet</p>');
                }
            }).catch(function(err){
                console.error('getCharactersByOwner ' + err  )
                $(".inventory-list").html('');
            });
}

// Update container of Create new Character
Character.prototype.updateCreateContainer = function() {
    var characterName = $("#create-name").val();
    var that = this;

    // Disallow negative numbers
    if(characterName.length > 0) {
        var address = window.top.web3.eth.accounts[0];
        this.getRandomDna(characterName, address, function(characterDna) {
                if(characterDna == 5142446803) {
                    var a = new Audio("https://studio.ethereum.org/static/img/cryptocharacter/1.mp3");
                    a.play();
                }
                var characterImage = that.generateCharacterImage(characterDna);
                $("#character-create-container .ingredients").html(characterImage);
            
        })
    }
    else {
        $("#character-create-container .ingredients").html('');
    }
}

// Generates images from DNA - returns all of them in HTML
Character.prototype.generateCharacterImage = function(dna) {
    var url = "https://studio.ethereum.org/static/img/cryptocharacter/";
    dna = dna.toString();
    var basis = (dna.substring(0, 2) % 2) + 1;
    var cheese = (dna.substring(2, 4) % 10) + 1;
    var meat = (dna.substring(4, 6) % 18) + 1;
    var spice = (dna.substring(6, 8) % 7) + 1;
    var veggie = (dna.substring(8, 10) % 22) + 1;

    var image = '';
    image += '<img src="'+url+'basis/basis-'+basis+'.png"/>';
    image += '<img src="'+url+'cheeses/cheese-'+cheese+'.png"/>';
    image += '<img src="'+url+'meats/meat-'+meat+'.png"/>';
    image += '<img src="'+url+'spices/spice-'+spice+'.png"/>';
    image += '<img src="'+url+'veggies/veg-'+veggie+'.png"/>';

    if(dna == 5142446803) {
        image = '<img src="https://studio.ethereum.org/static/img/cryptocharacter/basis/basis-2.png"/>\
                 <img src="https://studio.ethereum.org/static/img/cryptocharacter/meats/meat-13.png"/>\
                 <img src="https://studio.ethereum.org/static/img/cryptocharacter/8fe918632d847e8ea3ebffbd47bd8ca9.png"/>';
    }

    return image;
}

// Gift Character
Character.prototype.giftCharacter = function(characterId, cb) {
    var that = this;

    var sendTo = prompt("Enter address which should receive your Character");

    if(!isValidAddress(sendTo)) {
        showStatus("Please enter a valid address");
        return;
    }

    $(".button-gift, .button-eat").attr("disabled", true);
    $('#character-'+characterId).css("opacity", "0.7");

    var characterDna = $('#character-'+characterId +' .characterDna').attr('id');

    if(characterDna == 5142446803) {
        var a = new Audio("https://studio.ethereum.org/static/img/cryptocharacter/2.mp3");
        a.play();
    }

    // Gas and gasPrice should be removed for non browser networks
    this.instance.methods.transferFrom(window.top.web3.eth.accounts[0], sendTo, characterId).send({ from: window.top.web3.eth.accounts[0], gas: 100000, gasPrice: 1000000000, gasLimit: 100000 }).then(function( txHash) {
                showStatus("Sending Character...");
                that.waitForReceipt(txHash.transactionHash, function(receipt) {
                    if(receipt.blockNumber > 0) {
                        $('.inventory-list').html('');
                        $(".button-gift, .button-eat").attr("disabled", false);
                        showStatus("Character sent");
                        that.loadInventory();
                    }
                    else {
                        showStatus("Character was not sent. Please try it again.");
                        $(".button-gift, .button-eat").attr("disabled", false);
                        $('#character-'+characterId).css("opacity", "1");
                    }
                });
            }).catch(function(err){
               console.error(err);
                showStatus("Sending canceled.");
                $('#character-'+characterId).css("opacity", "1");
                return;
            });
        
}

// Eat Character
Character.prototype.eatCharacter = function(characterId, cb) {
    var that = this;

    var confirmation = confirm("Are you sure?")

    if(confirmation) {

        $(".button-gift, .button-eat").attr("disabled", true);
        $('#character-'+characterId).css("opacity", "0.7");

        var characterDna = $('#character-'+characterId +' .characterDna').attr('id');

        if(characterDna == 5142446803) {
            var a = new Audio("https://studio.ethereum.org/static/img/cryptocharacter/3.mp3");
            a.play();
        }

        // Gas and gasPrice should be removed for non browser networks
        this.instance.methods.burn(characterId ).send({ from: window.top.web3.eth.accounts[0], gas: 100000, gasPrice: 1000000000, gasLimit: 100000 }).then( function(txHash) {
                    showStatus("Eating Character...");
                    that.waitForReceipt(txHash.transactionHash, function(receipt) {
                        if(receipt.blockNumber > 0) {
                            $('.inventory-list').html('');
                            $(".button-gift, .button-eat").attr("disabled", false);
                            showStatus("Character is gone");
                            that.loadInventory();
                        }
                        else {
                            showStatus("Character was not eaten. Please try it again.");
                            $(".button-gift, .button-eat").attr("disabled", false);
                            $('#character-'+characterId).css("opacity", "1");
                        }
                    });
                } ).catch(function(err){
                 console.error(err);
                    $(".button-gift, .button-eat").attr("disabled", false);
                    $('#character-'+characterId).css("opacity", "1");
                    showStatus("Eating canceled.");
                    return;
            });
    
           
    } else {
        showStatus("Canceled");
    }
}

// Bind all inputs and buttons to specific functions
Character.prototype.bindInputs = function() {
    var that = this;
    var timeout = null; // Set timeout to every input so it doesn't fire too often

    $(document).on("change textInput input", "#create-name", function() {
        clearTimeout(timeout);
        timeout = setTimeout(function() {
            that.updateCreateContainer();
        }, 250);
    });

    $(document).on("click", "#button-create", function() {
        that.createRandomCharacter();
    });

    $(document).on("click", "button.button-gift", function() {
        var characterId = $(this).attr("id");
        that.giftCharacter(characterId);
    });

    $(document).on("click", "button.button-eat", function() {
        var characterId = $(this).attr("id");
        that.eatCharacter(characterId);
    });
    
     $(document).on("click", "#button-qr", function() {
        that.generateQrcode();
    });
}

// Show status on bottom of the page when some action happens
function showStatus(text) {
    var status = document.getElementById("status");
    status.innerHTML = text;
    status.className = "show";
    setTimeout(function(){ status.className = status.className.replace("show", ""); }, 3000);
}

// Check if provided address has the basic requirements of an address
function isValidAddress(address) {
    return /^(0x)?[0-9a-f]{40}$/i.test(address);
}

