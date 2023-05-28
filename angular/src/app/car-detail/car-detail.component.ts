import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';
import { CarsService } from '../cars-cards/cars-cards.service';
import { Coche } from './car.model';
import { HttpClient } from '@angular/common/http';


@Component({
  selector: 'app-car-detail',
  templateUrl: './car-detail.component.html',
  styleUrls: ['./car-detail.component.css']
})
export class CarDetailComponent implements OnInit {
  coche: any;

  constructor(
    private rutaCoche: ActivatedRoute,
    private carService: CarsService,
    private http:HttpClient
  ){ }

  ngOnInit(): void {
    const id = Number(this.rutaCoche.snapshot.paramMap.get('id'));
    this.carService.getCochesById(id).subscribe(coche => this.coche = coche);
  }

}
