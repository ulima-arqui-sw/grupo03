package com.grupo03.Lambda_Voyage.domain.repositories;

import com.grupo03.Lambda_Voyage.domain.entities.FlyEntity;
import com.grupo03.Lambda_Voyage.domain.entities.TicketEntity;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.repository.CrudRepository;

import java.util.UUID;


public interface TicketRepository extends CrudRepository<TicketEntity, UUID> {


}
