package com.ebiznes24.backend;

import dev.langchain4j.memory.chat.MessageWindowChatMemory;
import dev.langchain4j.model.chat.StreamingChatLanguageModel;
import dev.langchain4j.model.ollama.OllamaStreamingChatModel;
import dev.langchain4j.service.AiServices;
import dev.langchain4j.service.TokenStream;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.web.bind.annotation.*;

import java.time.Duration;
import java.util.concurrent.CompletableFuture;

@SpringBootApplication
public class Main {
    private static final String OLLAMA_HOST = "http://localhost:11434";
    private static final String MODEL_NAME = "llama2";

    public static void main(String[] args) {
        SpringApplication.run(Main.class, args);
    }

    @Bean
    public StreamingChatLanguageModel connectModel() {
        return OllamaStreamingChatModel.builder()
                .baseUrl(OLLAMA_HOST)
                .modelName(MODEL_NAME)
                .timeout(Duration.ofHours(1))
                .build();
    }

    @Bean
    public ModelCommunication assistant(StreamingChatLanguageModel model) {
        return AiServices.builder(ModelCommunication.class)
                .streamingChatLanguageModel(model)
                .chatMemory(MessageWindowChatMemory.withMaxMessages(5))
                .build();
    }

    @RestController
    @RequestMapping("/api/chat")
    public static class ChatController {

        private final ModelCommunication assistant;

        public ChatController(ModelCommunication assistant) {
            this.assistant = assistant;
        }

        @PostMapping
        public CompletableFuture<String> chat(@RequestBody String userPrompt) {
            CompletableFuture<String> responseFuture = new CompletableFuture<>();
            TokenStream tokenStream = assistant.chatWithModel(userPrompt);

            StringBuilder response = new StringBuilder();
            tokenStream.onNext(token -> {
                        response.append(token);
                        System.out.println("Received token: " + token);
                    })
                    .onComplete(x -> {
                        responseFuture.complete(response.toString());
                        System.out.println("Completed with response: " + response.toString());
                    })
                    .onError(ex -> {
                        responseFuture.completeExceptionally(ex);
                        System.err.println("Error occurred: " + ex.getMessage());
                    })
                    .start();

            return responseFuture;
        }
    }
}
