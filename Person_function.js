
const person ={
  myname: 'smith',
  introduce: function () {
     return 'hi i'm ${this.myname}'
  },
}

constbintroducer = person.introduce;

console.log(introducer());
