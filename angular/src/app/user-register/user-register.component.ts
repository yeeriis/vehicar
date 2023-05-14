import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-user-register',
  templateUrl: './user-register.component.html',
  styleUrls: ['./user-register.component.css']
})
export class UserRegisterComponent {
  // email: string;
  // password: string;
  // nombre: string;
  // apellido: string;
  // edad: number;
  // usuario: string;
  // foto: string;

  usuario = {}

  constructor(private http: HttpClient) {}

  register() {
    this.http.post('http://localhost:8000/api/usuarios/', this.usuario)
    .subscribe(response => {
        console.log(response);
      });
  }
}
