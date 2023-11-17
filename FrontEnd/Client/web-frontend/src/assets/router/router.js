import {createRouter,createWebHistory} from 'vue-router'
import ShoppingCart from '@/views/cart/ShoppingCart.vue'
import FastFoodMenu from '@/views/menu/Menu.vue'
const routers =[
    {
        path:"/cart",name:"cartRouter",component:ShoppingCart
    },
    {
        path:"/menu",name:"menuRouter",component:FastFoodMenu
    },
]
const vueRouter = createRouter({
    history: createWebHistory(),
    routes: routers
});

export default vueRouter;