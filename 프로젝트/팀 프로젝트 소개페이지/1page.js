package com.zipchatgo.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

import java.util.List;

@Controller
public class HomeController {

    @GetMapping("/")
    public String home(Model model) {

        List<String> news = List.of(
                "프로젝트 개발 시작",
                "UI 디자인 완료",
                "베타 서비스 준비"
        );

        model.addAttribute("newsList", news);

        return "index";
    }
}