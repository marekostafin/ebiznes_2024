package com.ebiznes2024;

import dev.langchain4j.memory.ChatMemory;
import dev.langchain4j.memory.chat.MessageWindowChatMemory;
import dev.langchain4j.model.chat.StreamingChatLanguageModel;
import dev.langchain4j.model.ollama.OllamaStreamingChatModel;
import dev.langchain4j.service.AiServices;
import dev.langchain4j.service.TokenStream;

import java.time.Duration;
import java.util.Scanner;
import java.util.concurrent.CompletableFuture;

public class Main {

    private static final String OLLAMA_HOST = "http://localhost:11434";
    private static final String MODEL_NAME = "llama2";

    private static StreamingChatLanguageModel connectModel() {
        return OllamaStreamingChatModel.builder()
                .baseUrl(OLLAMA_HOST)
                .modelName(MODEL_NAME)
                .timeout(Duration.ofHours(1))
                .build();
    }

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        var model = connectModel();
        var assistant = AiServices.builder(ModelCommunication.class)
                .streamingChatLanguageModel(model)
                .chatMemory(MessageWindowChatMemory.withMaxMessages(5))
                .build();


        while (true) {
            System.out.print("""
                    Type 'exit' to quit the program.
                    Enter your prompt:\s""");
            String userPrompt = scanner.nextLine();
            if (userPrompt.equals("exit")) {
                break;
            }

            TokenStream tokenStream = assistant.chatWithModel(userPrompt);
            CompletableFuture<Void> future = new CompletableFuture<>();
            tokenStream.onNext(System.out::print)
                    .onComplete(_ -> {
                        System.out.println();
                        future.complete(null);
                    })
                    .onError(Throwable::printStackTrace)
                    .start();
            future.join();
        }

    }

}