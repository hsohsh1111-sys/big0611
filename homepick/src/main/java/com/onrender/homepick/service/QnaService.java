package com.onrender.homepick.service;

import com.onrender.homepick.dto.QnaDto;
import com.onrender.homepick.repository.QnaRepository;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class QnaService{

    private final QnaRepository qnaRepository;

    public QnaService(QnaRepository qnaRepository){
        this.qnaRepository = qnaRepository;
    }

    public List<QnaDto> getAllQnaList(){
        return qnaRepository.findAll();
    }

    public void createQna(QnaDto qna){
        qnaRepository.save(qna);
    }
}