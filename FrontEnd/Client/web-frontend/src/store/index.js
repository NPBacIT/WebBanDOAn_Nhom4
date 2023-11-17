
import { createStore }  from 'vuex';


export const store = new createStore({
  state: {
    products: [],
    cart: JSON.parse(localStorage.getItem('cart')) || []
  },
  mutations: {
    setMaxQuantity(state, { productId, maxQuantity }) {
      const product = state.products.find(item => item.SoLuongMA === productId);
      if (product) {
        product.maxQuantity = maxQuantity;
      }
    },
    
    addToCart(state, product) {
      const cartItem = state.cart.find(item => item.MaMA === product.MaMA);
      if (cartItem) {
        cartItem.SoLuongMA += 1;
      } else {
        state.cart.push({ ...product, SoLuongMA: 1 });
      }
      store.commit('setMaxQuantity', { productId: product.MaMA, maxQuantity: product.SoLuongMA });
      localStorage.setItem('cart', JSON.stringify(state.cart));
    },
    removeFromCart(state, productId) {
      state.cart = state.cart.filter(item => item.MaMA !== productId);
      localStorage.setItem('cart', JSON.stringify(state.cart));
    },
    updateQuantity(state, payload) {
      const { productId, newQuantity } = payload;
      const cartItem = state.cart.find(item => item.MaMA === productId);
      const productInStore = state.products.find(item => item.MaMA === productId);
      if (cartItem && productInStore) {
        const quantityDifference = newQuantity - cartItem.SoLuongMA;

        cartItem.SoLuongMA = newQuantity;
          // Cập nhật số lượng sản phẩm trong cửa hàng
      productInStore.SoLuongMA -= quantityDifference;
      }
      localStorage.setItem('cart', JSON.stringify(state.cart));
    }
  },
  getters: {
    cartTotal(state) {
      return state.cart.reduce((total, item) => total + item.Gia * item.SoLuongMA, 0);
    }
  }
});