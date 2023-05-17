import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

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

  constructor(private http: HttpClient) {}

  register() {
    const data = { email: this.email, password: this.password };
    this.http.post('http://localhost:8000/api/auth/login/', data).subscribe(
      response => {
        console.log(response);
        alert("Acierto!")
      },
      error => {
        console.error(error);
        alert("Error!")
      }
    );
  }
}
