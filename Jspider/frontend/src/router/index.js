import Vue from 'vue'
import Router from 'vue-router'
import AddTask from '@/components/AddTask'
import Home from '@/components/Home'

Vue.use(Router)

//export default new Router({
//  routes: [
//    {
//    path: '/',
//    name: 'Wyyx',
//    component: Wyyx
//    }
//  ]
//})

const routes = [
    {
        path:"/",
        component: Home
    },
    {
        path: "/add_task",
        component: AddTask
    }
]

var router =  new Router({
    routes
})
export default router;

