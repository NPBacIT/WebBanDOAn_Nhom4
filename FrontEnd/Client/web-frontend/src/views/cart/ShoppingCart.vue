<template>
    <div>
    <h2>Shopping Cart</h2>
    <table>
      <thead>
        <tr>
          <th>Product</th>
          <!-- <th>Image</th> -->
          <th>Price</th>
          <th>Quantity</th>
          <th>Subtotal</th>
          <th>Action</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in cart" :key="item.MaMA">
  <td>{{ item.TenMA }}</td>
  
  <td>
    {{ item.Gia !== null && item.Gia !== undefined ? `$${item.Gia.toFixed(2)}` : 'N/A' }}
  </td>
  
  <td>
    <input type="number" v-model="item.SoLuongMA" @change="updateQuantity(item)" min="0" inputmode="numeric">
  </td>
  
  <td>
    {{ item.Gia !== null && item.Gia !== undefined && item.SoLuongMA !== null && item.SoLuongMA !== undefined ? `$${(item.Gia * item.SoLuongMA).toFixed(2)}` : 'N/A' }}
  </td>
  
  <td>
    <button @click="removeFromCart(item.MaMA)">Remove</button>
  </td>
</tr>
      </tbody>
    </table>
    <div>Total: {{ cartTotal }}$</div>
  </div>
</template>
<script>

export default{
 name:"ShoppingCart",
 computed: {
  cart() {
       return this.$store.state.cart;
      },
      cartTotal() {
      return this.$store.getters.cartTotal;
    }
 },
 methods: {

removeFromCart(productId) {
    this.$store.commit('removeFromCart', productId);
  
  },
  
  updateQuantity(item) {
    // Kiểm tra nếu số lượng vượt quá số lượng tối đa
    if (item.SoLuongMA < item.maxQuantity) {

      alert('Exceeds available quantity.');
      // Reset số lượng về số lượng tối đa
      item.SoLuongMA = item.maxQuantity;
    }
    if(item.SoLuongMA<0){
      item.SoLuongMA=0;
    }
   
    
    else {
      
      // Thực hiện cập nhật số lượng
      this.$store.commit('updateQuantity', { productId: item.MaMA, newQuantity: item.SoLuongMA });
    }
  },






 }

}
</script>
<style scoped>
  body, h1, h2, h3, p, ol, ul, li, table, td {
    margin: 0;
    padding: 0;
  }

  body {
    font-family: 'Arial', sans-serif;
    line-height: 1.6;
  }

  /* Style the shopping cart container */
  .shopping-cart {
    max-width: 800px;
    margin: 20px auto;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  }

  h2 {
    font-size: 24px;
    margin-bottom: 20px;
  }

  table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 20px;
  }

  th, td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
  }

  th {
    background-color: #f2f2f2;
  }

  input[type="number"] {
    width: 80px;
    padding: 5px;
    text-align: center;
  }

  button {
    padding: 5px 10px;
    background-color: #4caf50;
    color: #fff;
    border: none;
    border-radius: 3px;
    cursor: pointer;
  }

  button:hover {
    background-color: #45a049;
  }

  /* Style the total amount section */
  .total-section {
    font-size: 18px;
    font-weight: bold;
    margin-top: 20px;
  }
</style>