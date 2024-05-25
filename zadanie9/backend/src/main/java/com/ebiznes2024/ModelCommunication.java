package com.ebiznes2024;

import dev.langchain4j.service.TokenStream;

public interface ModelCommunication {

    TokenStream chatWithModel(String message);

}