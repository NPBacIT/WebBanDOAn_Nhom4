<script setup>
import Sidebar from '@/components/Sidebar.vue';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/dist/js/bootstrap.bundle.min';
import axios from 'axios'
</script>
<template>
    <Sidebar />
    <div class="container">
        <h3 class="mt-4 mb-3">Danh Sách Danh Mục Món Ăn</h3>
        <div class="row mb-3">
            <div class="col-md-6">
                <div class="input-group">
                </div>
            </div>
            <div class="col-md-6 text-right">
                <router-link to="/createCate">
                    <button type="button" class="btn btn-sm btn-danger">Create New</button>
                </router-link>
            </div>
        </div>
        <table class="table">
            <thead>
                <tr>
                    <th>ID</th>
                    <th style="width:20%">Tên Danh Mục</th>
                    <th></th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="cate in cates">
                    <th>{{ cate.MaLoaiMA }}</th>
                    <td>{{ cate.TenLoaiMA }}</td>
                    <td>
                       <button class="btn btn-sm btn-dark">
                        Edit
                       </button>
                            
                        &nbsp;
                        <button class="btn btn-sm btn-danger">Delete</button>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>
<script>
export default {
    name: 'listCategory',
    data() {
        return {
            cates: [],
            currentPage: 1,
            catesPerPage: 8,
        };
    },
    mounted() {
        this.fetchData();
    },
    methods: {
        fetchData() {
            axios.get(`http://103.69.195.147:23031/v1/items?table_name=LoaiMonAn&order_by_column=MaLoaiMA&page=${this.currentPage}&items_per_page=${this.itemsPerPage}`)
                .then(res => {
                    this.cates = res.data;
                })
                .catch(error => {
                    console.error('Error fetching data:', error);
                });
        }
    }
};
</script>


<style>
.pagination {
    position: fixed;
    /*can giua  */
    bottom: 20px;
    left: 50%;
    transform: translateX(-50%);
    align-items: center;
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 20px;
}

.pagination button {
    padding: 8px 12px;
    font-size: 14px;
    cursor: pointer;
    background-color: #4F46C5;
    color: white;
    border: none;
    border-radius: 4px;
}

.pagination button:disabled {
    background-color: #ddd;
    color: #666;
    cursor: not-allowed;
}

.pagination span {
    font-size: 16px;
    margin: 0 10px;
}
</style>