<script setup>
import Sidebar from '@/components/Sidebar.vue';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/dist/js/bootstrap.bundle.min';
import axios from 'axios'
</script>
<template>
  <Sidebar />
  <div class="container">
    <h3 class="mt-4 mb-3">Danh Sách Món Ăn</h3>
    <div class="row mb-3">
      <div class="col-md-6">
        <div class="input-group">
          <div class="input-group-prepend">
            <label class="input-group-text" for="price">Price:</label>
          </div>
          <select v-model="selectedPrice" class="custom-select" @change="filterItems" id="price" name="price">
            <option value="all">All</option>
            <option value="above">Above $17</option>
            <option value="below">Below $17</option>
          </select>
        </div>
      </div>
      <div class="col-md-6 text-right">
        <router-link to="/createDish">
          <button type="button" class="btn btn-sm btn-danger">Create New</button>
        </router-link>
      </div>
    </div>
    <table class="table">
      <thead>
        <tr>
          <th>ID</th>
          <th style="width:20%">Tên Món Ăn</th>
          <th>Giá</th>
          <th>Số lượng</th>
          <th>Active</th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in items">
          <th>{{ item.MaMA }}</th>
          <td>{{ item.TenMA }}</td>
          <td>{{ item.Gia }}</td>
          <td>{{ item.SoLuongMA }}</td>
          <td>
            <span v-if="item.Active === 0" class="badge badge-warning">Stocking</span>
            <span v-else-if="item.Active === 1" class="badge badge-success">No Stock</span>
          </td>
          <td>
            <router-link :to="{ name: 'Dish.update', params: { id: item.MaMA } }"
              class="btn btn-sm btn-dark">Edit</router-link>
            &nbsp;
            <button @click="deleteDish(item.MaMA)" class="btn btn-sm btn-danger">Delete</button>
          </td>
        </tr>
      </tbody>
    </table>
    <div class="pagination">
      <button @click="changePage('prev')" :disabled="currentPage === 1">Previous</button>
      <span v-if="totalPages > 0">{{ currentPage }} / {{ totalPages }}</span>
      <span v-else>1 / 1</span>
      <button @click="changePage('next')" :disabled="currentPage === totalPages">Next</button>
    </div>
  </div>
</template>





<script>
export default {
  name: 'listDish',
  data() {
    return {
      items: [],
      currentPage: 1,
      itemsPerPage: 8,
      totalItems: 0,
      totalPages: 10,
      selectedPrice: 'all',
    };
  },
  mounted() {
    this.fetchData();
  },
  methods: {
    fetchData() {
      axios.get(`http://103.69.195.147:23031/v1/items?table_name=MonAn&order_by_column=MaMA&page=${this.currentPage}&items_per_page=${this.itemsPerPage}`)
        .then(res => {
          this.items = res.data;
        })
        .catch(error => {
          console.error('Error fetching data:', error);
        });
    },
    deleteDish(itemId) {
      this.$swal.fire({
        title: 'Do you want to delete the changes?',
        showDenyButton: false,
        showCancelButton: true,
        confirmButtonText: 'OK',
      }).then((result) => {
        if (result.isConfirmed) {
          axios.delete(`http://103.69.195.147:23031/v1/delete_mon_an?MaMA=${itemId}`).then(res => {
            if (res.data) {
              this.$swal.fire(`Deleted!`, `Success`)
              this.fetchData();
            }
          })
        }
      })
    },
    changePage(action) {
      if (action === 'prev' && this.currentPage > 1) {
        this.currentPage--;
      } else if (action === 'next' && this.currentPage < this.totalPages) {
        this.currentPage++;
      }
      this.fetchData();
    },
    filterItems() {
      if (this.selectedPrice === 'all') {
        this.fetchData();
      } else if (this.selectedPrice === 'above') {
        this.items = this.items(item => item.Gia > 17);
      } else if (this.selectedPrice === 'below') {
        this.items = this.items.filter(item => item.Gia < 17);
      }
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