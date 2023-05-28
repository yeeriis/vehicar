import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import {Router} from '@angular/router';


@Component({
  selector: 'app-user-register',
  templateUrl: './user-register.component.html',
  styleUrls: ['./user-register.component.css']
})
export class UserRegisterComponent {
  email: string;
  password: string;
  nombre: string;
  apellido: string;
  edad: number;
  usuario: string;
  foto: string;

  constructor(private http: HttpClient, private router:Router) {}

  enviarFormulario() {

    const url = 'http://localhost:8000/api/register/';
    const formData = {
      email: this.email,
      password: this.password,
      nombre: this.nombre,
      apellido: this.apellido,
      edad: this.edad,
      usuario: this.usuario,
      foto: this.foto,
    }

    this.http.post( url, formData).subscribe(
      (response) => {
        console.log('Usuario creado correctamente:', response);
        this.router.navigate(['/login']);        
      },
      (error) => {
        console.log('Error al crear el usuario:', error);
      }
    );
  }

  registrarUsuario(formData: any) {
    const url = 'http://localhost:8000/api/register/';

    return this.http.get(url , formData);
  }
}

    