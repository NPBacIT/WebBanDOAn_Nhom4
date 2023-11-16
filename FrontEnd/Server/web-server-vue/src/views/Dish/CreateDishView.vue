<script setup >
import Sidebar from '@/components/Sidebar.vue';
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
            class="form-control" />
          <div class="invalid-feedback" v-if="errors.TenMA">{{ errors.TenMA }}</div>
        </div>
      </div>

      <div class="form-group row">
        <label for="ChiTietMA" class="col-sm-3 col-form-label">Chi tiết món ăn</label>
        <div class="col-sm-9">
          <input v-model="dish.ChiTietMA" @blur="validate()" v-bind:class="{ 'is-invalid': errors.ChiTietMA }"
            class="form-control" />
          <div class="invalid-feedback" v-if="errors.ChiTietMA">{{ errors.ChiTietMA }}</div>
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
        <label for="AnhMA" class="col-sm-3 col-form-label">Ảnh món ăn</label>
        <div class="col-sm-9">
          <input type="file" @change="handleFileChange" class="form-control" @blur="validate()"
            v-bind:class="{ 'is-invalid': errors.AnhMA }" />

        </div>
      </div>
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
            v-bind:class="{ 'is-invalid': errors.SoLuongMA }">
            <option value="" disabled selected>Select a type</option>
            <!-- Sử dụng v-for để tạo các tùy chọn từ danh sách loại món ăn -->
            <option v-for="loaiMonAn in danhSachLoaiMonAn" :key="loaiMonAn.MaLoaiMA" :value="loaiMonAn.MaLoaiMA">
              {{ loaiMonAn.TenLoaiMA }}
            </option>
          </select>
          <div class="invalid-feedback" v-if="errors.MaLoaiMA">{{ errors.MaLoaiMA }}</div>
        </div>
      </div>

      <div class="form-group row">
        <div class="col-sm-9 offset-sm-3">
          <button type="submit" class="btn btn-primary">Create</button> &nbsp;
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
        AnhMA: null,
        SoLuongMA: '',
        MaLoaiMA: '',
      },
      dish: {
        TenMA: '',
        ChiTietMA: '',
        Gia: '',
        AnhMA: null,
        SoLuongMA: '',
        MaLoaiMA: '',
      },
      danhSachLoaiMonAn: [],
    };
  },
  mounted() {
    this.fetchDanhSachLoaiMonAn();
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
        this.errors.ChiTietMA = 'Dish chitiet is required';

      }
      if (!this.dish.Gia) {
        this.errors.Gia = 'Dish price is required';
      } else if (!this.isNumber(this.dish.Gia)) {
        this.errors.Gia = 'Dish price must be a number';

      }
      if (!this.dish.SoLuongMA) {
        this.errors.SoLuongMA = 'Dish soluong is required';

      } else if (!this.isNumber(this.dish.SoLuongMA)) {
        this.errors.SoLuongMA = 'Dish soluong must be a number';

      }
      if (!this.dish.MaLoaiMA) {
        this.errors.MaLoaiMA = 'Dish description is required';

      }
    },
    isNumber(value) {
      return /^\d*$/.test(value);
    },
    submitForm() {
      if (this.validate()) {
        const fileName = this.dish.AnhMA ? this.dish.AnhMA.name : null;
        const payload = {
          TenMA: this.dish.TenMA,
          ChiTietMA: this.dish.ChiTietMA,
          Gia: Number.parseFloat(this.dish.Gia),
          AnhMA: fileName,
          SoLuongMA: Number.parseFloat(this.dish.SoLuongMA),
          MaLoaiMA: this.dish.MaLoaiMA,
        };

        axios.post(`http://103.69.195.147:23031/v1/add_mon_an?TenMA=${payload.TenMA}&ChiTietMA=${payload.ChiTietMA}&Gia=${payload.Gia}&AnhMA=${payload.AnhMA}&SoLuongMA=${payload.SoLuongMA}&MaLoaiMA=${payload.MaLoaiMA}`)
          .then(response => {
            if (response.data) {
              this.$swal.fire('Success', 'Dish added successfully', 'success')
              // Chuyển hướng sau khi thêm thành công
              this.$router.push('/listDish');
            }
          })
          .catch(error => {
            this.$swal.fire('Error', 'An error occurred while adding dish', error);
          });
      }
    },
    handleFileChange(event) {
      this.dish.AnhMA = event.target.files[0];
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
  