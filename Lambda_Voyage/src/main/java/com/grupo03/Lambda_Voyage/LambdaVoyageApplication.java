package com.grupo03.Lambda_Voyage;

import com.grupo03.Lambda_Voyage.domain.entities.ReservationEntity;
import com.grupo03.Lambda_Voyage.domain.entities.TicketEntity;
import com.grupo03.Lambda_Voyage.domain.entities.TourEntity;
import com.grupo03.Lambda_Voyage.domain.repositories.*;
import lombok.extern.slf4j.Slf4j;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import java.math.BigDecimal;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.UUID;

@SpringBootApplication
public class LambdaVoyageApplication {

	public static void main(String[] args) {
		SpringApplication.run(LambdaVoyageApplication.class, args);
	}
}
