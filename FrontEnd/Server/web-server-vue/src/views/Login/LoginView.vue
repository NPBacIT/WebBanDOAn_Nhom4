<template>
    <div class="login">
        <img class="img-bgr" src="../../assets/hero-bg.jpg" alt="">
        <div class="container-lg">
            <form @submit.prevent="login">
                <h2 class="mb-3">Login</h2>
                <div class="input">
                    <label for="email">UserName</label>
                    <input class="form-control" type="text" name="email" placeholder="username123" />
                </div>
                <div class="input">
                    <label for="password">Password</label>
                    <input class="form-control" type="password" name="password" placeholder="password123" />
                </div>
               
                    <div class="alternative-option mt-4">
                    You don't have an account? 
                    <router-link to="/signup" >
                    <span>Register</span>
                </router-link>
                </div>
                
                <button type="submit" class="mt-4 btn-pers" id="login_button">
                    Login
                </button>
                <div class="alert alert-warning alert-dismissible fade show mt-5 d-none" role="alert" id="alert_1">
                    Lorem ipsum dolor sit amet consectetur, adipisicing elit.
                    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                </div>
            </form>
        </div>
    </div>
</template>
  
<script>
// import { getAuth, signInWithEmailAndPassword } from "firebase/auth";

export default {
    data() {
        return {
            email: "",
            password: "",
        };
    },
    // methods: {
    //     login(submitEvent) {
    //         this.email = submitEvent.target.elements.email.value;
    //         this.password = submitEvent.target.elements.password.value;

    //         const auth = getAuth();
    //         signInWithEmailAndPassword(auth, this.email, this.password)
    //             .then(() => {
    //                 this.$router.push("/dashboard");
    //             })
    //             .catch((error) => {
    //                 const errorCode = error.code;
    //                 const errorMessage = error.message;
    //                 console.log(errorCode);
    //                 console.log(errorMessage);
    //                 let alert_1 = document.querySelector("#alert_1");
    //                 alert_1.classList.remove("d-none");
    //                 alert_1.innerHTML = errorMessage;
    //                 console.log(alert_1);
    //             });
    //     },
    //     moveToRegister() {
    //         this.$router.push("/register");
    //     },
    // },
};
</script>
<style>
.img-bgr {
    position: relative;
    width: 100%;
    height: 100%; /* Sử dụng chiều cao của viewport */
    overflow: hidden;
}

.mb-3{
    text-align: center;
}

.container-lg {
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

.container-lg {
    width: 500px;
    max-width: 95%
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
}</style>