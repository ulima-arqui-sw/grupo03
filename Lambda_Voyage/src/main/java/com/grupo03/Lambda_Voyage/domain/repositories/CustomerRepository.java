package com.grupo03.Lambda_Voyage.domain.repositories;

import com.grupo03.Lambda_Voyage.domain.entities.CustomerEntity;
import com.grupo03.Lambda_Voyage.domain.entities.FlyEntity;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.repository.CrudRepository;


public interface CustomerRepository extends CrudRepository<CustomerEntity, String> {


}
