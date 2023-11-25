package com.grupo03.Lambda_Voyage.aspects;

import org.aspectj.lang.JoinPoint;
import org.aspectj.lang.annotation.After;
import org.aspectj.lang.annotation.Aspect;
import org.springframework.stereotype.Component;

import java.util.Arrays;

@Component
@Aspect
public class NotifyAspect {

    @After(value = "@annotation(com.grupo03.Lambda_Voyage.util.annotations.Notify)")
    public void notifyInField(JoinPoint joinPoint){
        Arrays.stream(joinPoint.getArgs()).forEach(System.out::println);
    }
}
