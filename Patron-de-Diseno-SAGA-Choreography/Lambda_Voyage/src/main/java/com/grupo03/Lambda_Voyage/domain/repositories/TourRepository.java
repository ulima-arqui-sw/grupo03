package com.grupo03.Lambda_Voyage.domain.repositories;

import com.grupo03.Lambda_Voyage.domain.entities.FlyEntity;
import com.grupo03.Lambda_Voyage.domain.entities.TourEntity;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.repository.CrudRepository;


public interface TourRepository extends CrudRepository<TourEntity, Long> {


}
