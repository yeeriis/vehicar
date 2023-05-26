import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MainCarrouselComponent } from './main-carrousel.component';

describe('MainCarrouselComponent', () => {
  let component: MainCarrouselComponent;
  let fixture: ComponentFixture<MainCarrouselComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ MainCarrouselComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(MainCarrouselComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
