
import { createApp } from 'vue'
import App from './App.vue'
import axios from 'axios'
import { store } from './store'
import vueRouter from './assets/router/router.js'
 // Đảm bảo đường dẫn đúng

import TheToast from './components/Toast.vue'

const app = createApp(App)
app.use(store)
app.config.globalProperties.$axios=axios
app.component("m-toast", TheToast)
app.use(vueRouter)


app.mount('#app')

