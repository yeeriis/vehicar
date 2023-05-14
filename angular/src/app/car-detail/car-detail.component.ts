import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';
import { CarsService } from '../cars-cards/cars-cards.service';
import { Coche } from './car.model';

@Component({
  selector: 'app-car-detail',
  templateUrl: './car-detail.component.html',
  styleUrls: ['./car-detail.component.css']
})
export class CarDetailComponent implements OnInit {
  car: Coche;

  constructor(
    private route: ActivatedRoute,
    private carService: CarsService,
    private location: Location
  ){ }

  ngOnInit(): void {
    const id = Number(this.route.snapshot.paramMap.get('id'));
    this.carService.getCars().subscribe(car => {
      this.car = car;
    });
  }

  goBack(): void {
    this.location.back();
  }
}
