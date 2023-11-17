<template>
  <TheHeader></TheHeader>
  <TheContent></TheContent>
  <TheFooter></TheFooter>
 
</template>

<script>

import TheHeader from './components/TheHeader.vue'
import TheFooter from './components/TheFooter.vue'
import TheContent from './components/TheContent.vue'
export default {
  name: 'App',
  components: {
    TheHeader,TheContent,TheFooter,
  }
}
</script>

<style scoped>
@import url(./css/view/bootstrap.css);

@import url(./css/view/responsive.css);

@import url(./css/view/style.css);

@import url(https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css); 

</style>
