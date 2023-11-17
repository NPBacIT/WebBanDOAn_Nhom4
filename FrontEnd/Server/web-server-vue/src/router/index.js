import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/listDish',
    name: 'listDish',
    component: () => import('../views/Dish/DishView.vue')
  },
  {
    path: '/createDish',
    name: 'Dish.create',
    component: () => import('../views/Dish/CreateDishView.vue')
  },
  {
    path: '/updateDish:id',
    name: 'Dish.update',
    component: () => import('../views/Dish/UpdateDishView.vue')
  },
  {
    path: '/login',
    name: 'Login.login',
    component: () => import('../views/Login/LoginView.vue')
  },
  {
    path: '/signup',
    name: 'Login.signup',
    component: () => import('../views/Login/SignUpView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
