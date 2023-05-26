import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-car-leasing',
  templateUrl: './car-leasing.component.html',
  styleUrls: ['./car-leasing.component.css']
})
export class CarLeasingComponent{
  email_usuario:string;
  coche_alquilado:string;
  fecha_inicio_alquiler:string;
  fecha_fin_alquiler:string;
  precio_alquiler:string;

  constructor(private http:HttpClient, private router:Router){ }

  alquiler() {

    const url = 'http://localhost:8000/api/register-leasing/';
    const formData = {
      email_usuario: this.email_usuario,
      coche_alquilado: this.coche_alquilado,
      fecha_inicio_alquiler: this.fecha_inicio_alquiler,
      fecha_fin_alquiler: this.fecha_fin_alquiler,
      precio_alquiler: this.precio_alquiler,
    }

    this.http.post( url, formData).subscribe(
      (response) => {
        // console.log('Usuario creado crrectamente:', response);
        this.router.navigate(['']);        
      },
      (error) => {
        console.log('Error al crear el alquiler:', error);
      }
    );
  }

  registrarAlquiler(formData: any) {
    const url = 'http://localhost:8000/api/register-leasing/';

    return this.http.get(url, formData);
  }
  // ngOnInit(): void {
  //   const id = Number(this.rutaCoche.snapshot.paramMap.get('id'));
  //   this.carService.getCochesById(id).subscribe(coche => this.coche = coche);
  // }

}
