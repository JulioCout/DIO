const bip32 = require('bip32')
const bip39 = require('bip39')
const bitcoin = require('bitcoinjs-lib')

//definição de rede
const network = bitcoin.networks.testnet

//derivação de carteiras HD
const path = `m/49'/1'/0'/0`

//definição de mnemonic
let mnemonic = bip39.generateMnemonic()
const seed = bip39.mnemonicToSeedSync(mnemonic)

//cria raiz da carteira HD
let root = bip32.fromSeed(seed, network)

//cria conta
let account = root.derivePath(path)
let node = account.derive(0).derive(0)

let btcAdress = bitcoin.payments.p2pkh({
    pubkey: node.publicKey,
    network: network,

}).address

console.log("Endereço: ", btcAdress)
console.log("Chave Privada: ", node.toWIF())
console.log("Seed: ", mnemonic)