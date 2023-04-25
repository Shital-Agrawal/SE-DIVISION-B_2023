const tr = require("googletrans").default;

const js = {
  _id: "6311f2815ff7c71aa1f78429",
  deleted: false,
  ticketNumber: "225",
  subject: "lite tankar",
  description:
    "Hej.\nHar lite tankar och ideer som jag har samt frått från andra som använder plattformarna. \nNär det gäller dNFT plattformen hade det varit bra om man kunde klicka sig direkt från låten till handelsplattformen. Alltså om man ser på de avslutatde kampanjerna så skulle det finnas en direktlänk dit där man kan köpa dessa tokens.\n\nSen var det en som önskade en dela knapp på NFT sidan, så man direkt kan dela till olika medier.\n\nlite input bara :)\n\nha en go helg!",
  createdBy: "603e777bd354dd0b214689fd",
  creatorEmail: "daniel.berglov@gmail.com",
  status: "NOT_RESOLVED",
  ticketType: "USER",
  createdFor: { type: "ADMIN" },
  created_at: "2022-09-02T12:09:37.642Z",
  updated_at: "2022-09-02T12:09:37.642Z",
  __v: 0,
};
const main = async () => {
  const subject = await tr(js.subject),
    created_at = new Date(js.created_at),
    description = await tr(js.description),
    ticketNumber = js.ticketNumber,
    statusTicket = js.status,
    createdBy = js.createdBy,
    createdFor = js.createdFor;

  let message = `Subject: ${subject.text}\nDate: ${
    created_at.getDay() +
    "/" +
    created_at.getMonth() +
    "/" +
    created_at.getFullYear()
  }\n\n${
    description.text
  }\n\nTicket Number: ${ticketNumber}\nStatus: ${statusTicket}\nCreated By: ${createdBy}\nCreated For: ${
    createdFor.type
  }\n`;

  console.log(message);
};
main();
