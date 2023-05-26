import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CarLeasingComponent } from './car-leasing.component';

describe('CarLeasingComponent', () => {
  let component: CarLeasingComponent;
  let fixture: ComponentFixture<CarLeasingComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CarLeasingComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CarLeasingComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
