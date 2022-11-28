<template>
    <div>
        <div class="info">
                <h2>Registrar Arbitro</h2>
                <h5>Ingresa los campos para dar de alta un nuevo arbitro</h5>
                <div class="form">   
                    <b-form @submit.prevent="addReferee()">
    
                        <b-form-group id="input-group-1" label="Nombre:" label-for="input-1">
                            <b-form-input
                            id="input-1"
                            v-model="first_name"
                            placeholder="Nombre"
                            required
                            ></b-form-input>
                        </b-form-group>
                        <b-form-group id="input-group-2" label="Apellido:" label-for="input-2">
                            <b-form-input
                            id="input-2"
                            v-model="last_name"
                            placeholder="Apellido"
                            required
                            ></b-form-input>
                        </b-form-group>
                        <b-form-group id="input-group-3" label="Numero de telefono:" label-for="input-3">
                            <b-form-input
                            id="input-3"
                            v-model="phone_number"
                            placeholder="Numero de telefono"
                            required
                            ></b-form-input>
                        </b-form-group>
                        <b-form-group id="input-group-4" label="Correo Electronico:" label-for="input-4">
                            <b-form-input
                            id="input-4"
                            type="email"
                            v-model="email"
                            placeholder="Correo Electronico"
                            required
                            ></b-form-input>
                        </b-form-group>
                        <b-form-group id="input-group-5" label="Contraseña:" label-for="input-5">
                            <b-form-input
                            id="input-5"
                            type="password"
                            v-model="password"
                            placeholder="Contraseña"
                            required
                            ></b-form-input>
                        </b-form-group>
                        <b-form-group id="input-group-6" label="Confirmar Contraseña:" label-for="input-6">
                            <b-form-input
                            id="input-6"
                            type="password"
                            v-model="repassword"
                            placeholder="Confirmar Contraseña"
                            required
                            ></b-form-input>
                        </b-form-group>
                        <b-button type="submit" variant="primary">Registrar Arbitro</b-button>
    
                    </b-form>
                </div>
        </div>        
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'AddReferee',

    data() {
        return {
            first_name: '',
            last_name: '',
            phone_number: '',
            email: '',
            password: '',
            repassword: '',
            referee_status: true
        }
    },
    methods: {
        async addReferee() {
            const data = { first_name: this.first_name, last_name: this.last_name, phone_number: this.phone_number, 
                           is_referee: this.referee_status, email: this.email, password: this.password, re_password: this.repassword };
            const response = await axios.post('http://127.0.0.1:8000/auth/users/', data) 
            this.goToTeam()
        
        },
        goToTeam() {
            alert("Arbitro agregado correctamente")
            this.$router.back() 
        }
    },
}
</script> 

<style scoped>
.info {
    flex: 80%;
    margin: 15px;
    text-align: left;
}
.form {
    margin:  25px 50px 0 50px;

}
h2 {
    border-bottom: 1px solid black;
    text-align: left;
}
</style>