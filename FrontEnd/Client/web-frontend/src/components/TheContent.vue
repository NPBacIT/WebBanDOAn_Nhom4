<template>
<router-view></router-view>
  
  <!-- end book section -->
</template>
<script>


export default{
 name:"TheContent",
 created(){
  

 },

 computed: {
  cart() {
       return this.$store.state.cart;
      },
      cartTotal() {
      return this.$store.getters.cartTotal;
    }
 },
 methods: {

  
  

  
  
 
 },
 data() {
  return {
    showToast: false,
    toastMessage: 'Toast Message!',
    products: [],
    imgName: '',
  }
 },

}
</script>
<style scoped>
 

</style>