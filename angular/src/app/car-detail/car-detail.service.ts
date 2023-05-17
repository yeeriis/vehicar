import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Coche } from '../car-detail/car.model';
import { map } from 'rxjs/operators';



@Injectable({
  providedIn: 'root'
})
export class CarDetailService {

  baseUrl = 'http://localhost:8000/api/coches';

  constructor(private http: HttpClient) { }

  getCochesById(id: number): Observable<Coche>{
    const url = `${this.baseUrl}/${id}`;
    console.log(url);
    return this.http.get<Coche>(url).pipe( map((response: any) => {
      return response.coche;})
    );
  }

  
}
