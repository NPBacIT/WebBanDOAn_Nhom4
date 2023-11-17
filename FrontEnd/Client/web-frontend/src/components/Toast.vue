
<template>
    <div class="toast-container" id="toastContainer">
    <div class="toast" id="toast">
      This is a simple toast message.
    </div>
  </div>
</template>

<script>
export default {
  name:"TheToast",
  props: {
    visible: {
      type: Boolean,
      default: false,
    },
    message: {
      type: String,
      default: '',
    },
  },
};
</script>

<style>
/* Add your styling for the toast message here */
.toast {
  background-color: #bd1f1f;
  color: #050505;
  padding: 15px;
  position: fixed;
  top: 16px; /* Adjust as needed */
  right: 16px; /* Adjust as needed */
  z-index: 10;
  transition: opacity 0.5s; /* Adjust the duration as needed */
}

.fade-enter-active, .fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter, .fade-leave-to {
  opacity: 0;
}
</style>