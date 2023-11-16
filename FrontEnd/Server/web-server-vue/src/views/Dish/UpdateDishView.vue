<script setup >
import Sidebar from '@/components/Sidebar.vue';
import router from '@/router';
import { ref } from 'vue';
import { useRoute } from 'vue-router';


</script>
<template>
  <Sidebar />
  <div class="container">
    <form @submit.prevent="submitForm()" enctype="multipart/form-data">
      <div class="pricing-header px-3 py-3 pt-md-5 pb-md-4 mx-auto text-center">
        <h3 class="display-5">Thêm món ăn</h3>
      </div>

      <div class="form-group row">
        <label for="TenMA" class="col-sm-3 col-form-label">Tên món ăn</label>
        <div class="col-sm-9">
          <input v-model="dish.TenMA" @blur="validate()" v-bind:class="{ 'is-invalid': errors.TenMA }"
            class="form-control" readonly />
        </div>
      </div>

      <div class="form-group row">
        <label for="ChiTietMA" class="col-sm-3 col-form-label">Chi tiết món ăn</label>
        <div class="col-sm-9">
          <input v-model="dish.ChiTietMA" @blur="validate()" v-bind:class="{ 'is-invalid': errors.ChiTietMA }"
            class="form-control" readonly />
        </div>
      </div>

      <div class="form-group row">
        <label for="Gia" class="col-sm-3 col-form-label">Giá</label>
        <div class="col-sm-9">
          <input v-model="dish.Gia" @blur="validate()" v-bind:class="{ 'is-invalid': errors.Gia }" class="form-control" />
          <div class="invalid-feedback" v-if="errors.Gia">{{ errors.Gia }}</div>
        </div>
      </div>
      <div class="form-group row">
        <label for="Gia" class="col-sm-3 col-form-label">Ảnh món ăn</label>
        <div class="col-sm-9">
          <input v-model="dish.AnhMA" @blur="validate()" v-bind:class="{ 'is-invalid': errors.AnhMA }"
            class="form-control" readonly />
        </div>
      </div>
      <!-- <div class="form-group row">
        <label for="AnhMA" class="col-sm-3 col-form-label">Ảnh món ăn</label>
        <div class="col-sm-9">
          <input type="file" @change="handleFileChange" class="form-control" @blur="validate()" v-bind:class="{ 'is-invalid': errors.AnhMA }" />
        </div>
      </div> -->
      <div class="form-group row">
        <label for="SoLuongMA" class="col-sm-3 col-form-label">Số lượng món ăn</label>
        <div class="col-sm-9">
          <input v-model="dish.SoLuongMA" @blur="validate()" v-bind:class="{ 'is-invalid': errors.SoLuongMA }"
            class="form-control" />
          <div class="invalid-feedback" v-if="errors.SoLuongMA">{{ errors.SoLuongMA }}</div>
        </div>
      </div>

      <div class="form-group row">
        <label for="MaLoaiMA" class="col-sm-3 col-form-label">Loại món ăn</label>
        <div class="col-sm-9">
          <select v-model="dish.MaLoaiMA" class="form-control" @blur="validate()"
            v-bind:class="{ 'is-invalid': errors.SoLuongMA }" disabled>
            <option value="" disabled selected>Select a type</option>
            <option v-for="loaiMonAn in danhSachLoaiMonAn" :key="loaiMonAn.MaLoaiMA" :value="loaiMonAn.MaLoaiMA">
              {{ loaiMonAn.TenLoaiMA }}
            </option>
          </select>
        </div>
      </div>

      <div class="form-group row">
        <div class="col-sm-9 offset-sm-3">
          <button type="submit" class="btn btn-primary">Save</button> &nbsp;
          <router-link to="/listDish"><button class="btn btn-danger">Back</button></router-link>
        </div>
      </div>
    </form>
  </div>
</template>
<script>
import axios from 'axios';
export default {
  name: 'DishForm',
  components: {
    Sidebar,
  },
  data() {
    return {
      errors: {
        TenMA: '',
        ChiTietMA: '',
        Gia: '',
        AnhMA: '',
        SoLuongMA: '',
        MaLoaiMA: '',
      },
      dish: {
        MaMA: '',
        TenMA: '',
        ChiTietMA: '',
        Gia: '',
        AnhMA: '',
        SoLuongMA: '',
        MaLoaiMA: '',
      },
      danhSachLoaiMonAn: [],
    };
  },
  mounted() {
    this.fetchDanhSachLoaiMonAn();
  },
  created() {
    const route = useRoute();
    const dishId = ref(route.params.id);
    if (dishId.value) {
      this.getDish(dishId.value);
    }
  },
  methods: {
    // Hàm để gọi API lấy danh sách loại món ăn
    fetchDanhSachLoaiMonAn() {
      axios.get('http://103.69.195.147:23031/v1/items?table_name=LoaiMonAn&order_by_column=MaLoaiMA')
        .then(response => {
          this.danhSachLoaiMonAn = response.data;
        })
        .catch(error => {
          console.error('Error fetching danh sach loai mon an:', error);
        });
    },
    validate() {
      this.errors = {
        TenMA: '',
        ChiTietMA: '',
        Gia: '',
        AnhMA: null,
        SoLuongMA: '',
        MaLoaiMA: '',
      };
      if (!this.dish.TenMA) {
        this.errors.TenMA = 'Dish name is required';

      }
      if (!this.dish.ChiTietMA) {
        this.errors.ChiTietMA = 'dish chitiet is required';

      }
      if (!this.dish.Gia) {
        this.errors.Gia = 'dish price is required';

      } else if (!this.isNumber(this.dish.Gia)) {
        this.errors.Gia = 'dish price must be a number';

      }
      if (!this.dish.SoLuongMA) {
        this.errors.SoLuongMA = 'dish SOLUONG is required';

      } else if (!this.isNumber(this.dish.SoLuongMA)) {
        this.errors.SoLuongMA = 'dish SOLUONG must be a number';

      }
      if (!this.dish.MaLoaiMA) {
        this.errors.MaLoaiMA = 'dish description is required';

      }

    },
    isNumber(value) {
      return /^\d*$/.test(value);
    },
    submitForm() {
      if (this.validate()) {
        const payload = {
          MaMA: this.dish.MaMA,
          TenMA: this.dish.TenMA,
          ChiTietMA: this.dish.ChiTietMA,
          Gia: Number.parseFloat(this.dish.Gia),
          AnhMA: this.dish.AnhMA,
          SoLuongMA: Number.parseFloat(this.dish.SoLuongMA),
          MaLoaiMA: this.dish.MaLoaiMA,
        };
        axios.patch(`http://103.69.195.147:23031/v1/update_mon_an?MaMA=${payload.MaMA}&Gia=${payload.Gia}&SoLuongMA=${payload.SoLuongMA}`)
          .then(response => {
            if (response.data) {
              this.$swal.fire('Success', 'Dish updated successfully', 'success')
              this.$router.push('/listDish');// Back DishView
            }
          })

          .catch(error => {
            this.$swal.fire('Error', 'An error occurred while updated dish', error);
          });
      }
    },
    handleFileChange(event) {
      this.dish.AnhMA = event.target.files[0];
    },
    // Gọi hàm để lấy món ăn 
    getDish(dishId) {
      axios.get(`http://103.69.195.147:23031/v1/item?table_name=MonAn&table_key=MaMA&value=${dishId}`)
        .then(res => {
          this.dish = res.data
          //console.log(this.dish);
        });
    },
  },
};
</script>




<style scoped>
.card-deck {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.card {
  margin-bottom: 15px;
}

table {
  margin-top: 20px;
}
</style>
  