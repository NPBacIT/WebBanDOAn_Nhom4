<template>
    <div class="register">
        <img class="img-bgr" src="../../assets/hero-bg.jpg" alt="">
        <div class="container">
            <form @submit.prevent="register">
                <h2 class="mb-3">Register</h2>
                <div class="input">
                    <label for="fullname">FullName</label>
                    <input class="form-control" v-model="user.fullname"  @blur="validate()" :class="{ 'is-invalid': errors.fullname }"  type="text" name="fullname" placeholder="Tran Van A" />
                    <div class="invalid-feedback" v-if="errors.fullname">{{ errors.fullname }}</div>
                </div>
                <div class="input">
                    <label for="username">Username</label>
                    <input class="form-control" v-model="user.username" @blur="validate()" :class="{ 'is-invalid': errors.username }" type="text" name="username" placeholder="username123" />
                    <div class="invalid-feedback" v-if="errors.username">{{ errors.username }}</div>
                </div>
                <div class="input">
                    <label for="email">Email</label>
                    <input class="form-control" v-model="user.email" @blur="validate()" :class="{ 'is-invalid': errors.email }" type="text" name="email" placeholder="email@address.com" />
                    <div class="invalid-feedback" v-if="errors.email">{{ errors.email }}</div>
                </div>
                <div class="input">
                    <label for="password">Password</label>
                    <input class="form-control" v-model="user.password" @blur="validate()" :class="{ 'is-invalid': errors.password }" type="password" name="password" placeholder="password123" />
                    <div class="invalid-feedback" v-if="errors.password">{{ errors.password }}</div>
                </div>
                <div class="input">
                    <label for="phone">Phone</label>
                    <input class="form-control" v-model="user.phone" @blur="validate()" :class="{ 'is-invalid': errors.phone }" type="text" name="text" placeholder="0123456789" />
                    <div class="invalid-feedback" v-if="errors.phone">{{ errors.phone }}</div>
                </div>
                <div class="input">
                    <label for="address">Address</label>
                    <input class="form-control" v-model="user.address" @blur="validate()" :class="{ 'is-invalid': errors.address }" type="address" name="address" placeholder="Ha Noi" />
                    <div class="invalid-feedback" v-if="errors.address">{{ errors.address }}</div>
                </div>
                <div class="alternative-option mt-4">
                    Already have an account?
                    <router-link to="/login">
                        <span>Login</span>
                    </router-link>
                </div>
                <button type="submit" class="mt-4 btn-pers" id="register_button">
                    Register
                </button>
                <div class="alert alert-warning alert-dismissible fade show mt-5 d-none" role="alert" id="alert_2">
                    Lorem ipsum dolor sit amet consectetur, adipisicing elit.
                    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      user: {
        fullname: '',
        username: '',
        email: '',
        password: '',
        phone: '',
        address: '',
      },
      errors: {
        fullname: '',
        username: '',
        email: '',
        password: '',
        phone: '',
        address: '',
      },
    };
  },
  methods: {
    register() {
      if (this.validate()) {
        console.log('Form is valid. Proceed with registration.');
      } else {
        console.log('Form is invalid. Please correct errors.');
      }
    },
    validate() {
      let isValid = true;
      // Reset errors
      this.errors = {
        fullname: null,
        username: null,
        email: '',
        password: '',
        phone: '',
        address: '',
      };

      // Validate each field
      if (!this.user.fullname) {
        this.errors.fullname = 'Full Name is required';
        isValid = false;
      }
      if (!this.user.username) {
        this.errors.username = 'Username is required';
        isValid = false;
      }
      if (!this.user.email) {
        this.errors.email = 'Email is required';
        isValid = false;
      } else if (!this.validateEmail(this.user.email)) {
        this.errors.email = 'Please enter a valid email address';
        isValid = false;
      }
      if (!this.user.password) {
        this.errors.password = 'Password is required';
        isValid = false;
      }
      if (!this.user.phone) {
        this.errors.phone = 'Phone is required';
        isValid = false;
      } else if (!this.validatePhone(this.user.phone)) {
        this.errors.phone = 'Please enter a valid phone number';
        isValid = false;
      }
      if (!this.user.address) {
        this.errors.address = 'Address is required';
        isValid = false;
      }
      return isValid;
    },
    validateEmail(email) {
      // Your email validation logic here
      // Return true if email is valid, false otherwise
      return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
    },
    validatePhone(phone) {
      // Your phone number validation logic here
      // Return true if phone is valid, false otherwise
      return /^\d{10}$/.test(phone);
    },
    register(){
      if (this.validate()){
        const payload = {
          fullname: this.user.fullname,
          username: this.user.username,
          email: this.user.email,
          password: this.user.password,
          phone: Number.parseFloat(this.user.phone),
          address: this.user.address,
        };
        
      }
    }
  },
};
</script>

<style>
.img-bgr {
    position: relative;
    width: 100%;
    height: 100%;
    overflow: hidden;
}

.mb-3 {
    text-align: center;
}

.container {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    border: 1px solid #d3d3d3;
    padding: 4rem 4rem;
    border-radius: 5px;
    background: #fafafa;
}

.background {
    width: 100vw;
    height: 100vh;
    position: absolute;
    background: #fafafa
}

.container {
    width: 600px;
    max-width: 100%
}

.input {
    display: flex;
    flex-direction: column;
    margin-bottom: 15px
}

.input>label {
    text-align: start
}

.input>input {
    margin-top: 6px;
    height: 38px !important
}

.btn-pers {
    position: relative;
    left: 50%;
    padding: 1em 2.5em;
    font-size: 12px;
    text-transform: uppercase;
    letter-spacing: 2.5px;
    font-weight: 700;
    color: #000;
    background-color: #fff;
    border: none;
    border-radius: 45px;
    box-shadow: 0 8px 15px rgba(0, 0, 0, .1);
    transition: all .3s ease 0s;
    cursor: pointer;
    outline: none;
    transform: translateX(-50%)
}

.btn-pers:hover {
    background-color: #198754;
    box-shadow: 0 15px 20px rgba(46, 229, 157, .4);
    color: #fff;
    transform: translate(-50%, -7px)
}

.btn-pers:active {
    transform: translate(-50%, -1px)
}

.alternative-option {
    text-align: center
}

.alternative-option>span {
    color: #0d6efd;
    cursor: pointer
}

#sign_out {
    position: relative;
    left: 50%;
    transform: translateX(-50%)
}
</style>