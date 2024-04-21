const cashRegister = {
    itemsForSale: {
      Phone: 300,
      "Smart TV": 220,
      "Gaming Console": 150,
    },
    shoppingCart: [],
    addItem: function (itemName) {
      if (this.itemsForSale[itemName] !== undefined) {
        this.shoppingCart.push(itemName);
        console.log(`${itemName} added to the shopping cart.`);
      } else {
        console.log(`We don't sell ${itemName}.`);
      }
    },
    calculateTotalPrice: function () {
      let totalPrice = 0;
      for (let item of this.shoppingCart) {
        totalPrice += this.itemsForSale[item];
      }
      return totalPrice;
    },
    pay: function (paymentAmount) {
      let totalPrice = this.calculateTotalPrice();
      let discount = 0;
      if (totalPrice > 400) {
        discount = totalPrice * 0.1;
      }
      totalPrice -= discount;
      console.log(`Total price: $${totalPrice}`);
      if (paymentAmount >= totalPrice) {
        let change = paymentAmount - totalPrice;
        console.log(`Thank you for your purchase! Your change is $${change}.`);
      } else {
        console.log(`You don't have enough money to purchase the items.`);
      }
    },
  };
  
  // Test the cash register
  cashRegister.addItem("Iphone");
  cashRegister.addItem("Smart TV");
  cashRegister.addItem("Phone")
  cashRegister.addItem("Gaming Console");
  console.log(`Total price: $${cashRegister.calculateTotalPrice()}`);
  cashRegister.pay(800);
  