const bitwala = require('bitwala');

const client = bitwala.client({
  env: 'dev',
  token: {
    _id: 'JqPp9cX7orLSbrhZM',
    secret: 'Mo4JGEhaANhLO7wWrzIvbNoXYPdPrVZXIUMu+gW/Ug1wtQgaVDAlypPXqLrq9DxX'
  }
});

// Info
// client.info()
//   .then(console.log)
//   .catch(console.log)

// client.info(console.log)

//
//
// client.info('inputs')
//   .then(console.log)
//   .catch(console.log)
//
//
// client.info('outputs')
//   .then(console.log)
//   .catch(console.log)

// auth
// client.auth()
//   .then(console.log)
//   .catch(console.log)
//
// // transactions
// client.transactions.get({page: 1})
//   .then(console.log)
//   .catch(console.log)
//
// client.transactions.get({_id: '123'})
//   .then(console.log)
//   .catch(console.log)
//
// client.transactions.get({ref: '123'})
//   .then(console.log)
//   .catch(console.log)
//
// client.transactions.create({
//   ref: 'My custom id',
//   inputs: [{
//     collection: 'BitcoinInvoices',
//     doc: {
//       currency: 'XBT',
//       convertedCurrency: 'EUR',
//       convertedAmount: 100
//     }
//   }],
//   outputs: [{
//     collection: 'BankTransfers',
//     doc: {
//       amount: 100,
//       currency: 'EUR',
//       reference: 'January Salary',
//       bankAccount: {
//         recipientType: 'INDIVIDUAL',
//         firstName: 'Satoshi',
//         lastName: 'Nakamoto',
//         iban: 'DE89370400440532013000',
//         currency: 'EUR'
//       }
//     }
//   }]
// }).then(r => console.log(r))
//   .catch(err => console.log(err));

client.transactions.cancel({transactionId: 'Zn9thp8PM8tQq3dDW'}, console.log)
