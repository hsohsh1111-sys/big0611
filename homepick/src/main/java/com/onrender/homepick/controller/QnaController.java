package com.onrender.homepick.controller;

import com.onrender.homepick.dto.QnaDto;
import com.onrender.homepick.service.QnaService;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@Controller
@RequestMapping("/qna")
public class QnaController{

    private final QnaService qnaService;

    public QnaController(QnaService qnaService){
        this.qnaService = qnaService;
    }

    // 게시판 목록 페이지
    @GetMapping("/list")
    public String list(Model model){
        List<QnaDto> qnaList = qnaService.getAllQnaList();
        model.addAttribute("qnaList", qnaList);
        model.addAttribute("totalCount", qnaList.size());
        return "qna/list";
    }

    // 질문 작성 폼 페이지 (추후 구현)
    @GetMapping("/write")
    public String writeForm(){
        return "qna/write";
    }
}