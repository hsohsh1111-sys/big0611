package com.onrender.homepick.controller;

import com.onrender.homepick.dto.MemberJoinDto;
import com.onrender.homepick.service.MemberService;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;

@Controller
public class MemberController{

    private final MemberService memberService;

    public MemberController(MemberService memberService){
        this.memberService = memberService;
    }

    @GetMapping("/login")
    public String loginPage(){
        return "member/login";
    }

    @GetMapping("/join")
    public String joinPage(){
        return "member/join";
    }

    // 회원가입 처리
    @PostMapping("/join")
    public String joinProcess(@ModelAttribute MemberJoinDto joinDto){
        memberService.join(joinDto);
        return "redirect:/login"; // 가입 성공 시 로그인 페이지로 이동
    }
}