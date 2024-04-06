package com.ebiznes

import discord4j.core.DiscordClientBuilder
import discord4j.core.event.domain.lifecycle.ReadyEvent
import discord4j.core.event.domain.message.MessageCreateEvent
import discord4j.core.`object`.entity.Message

fun main() {

    val botToken = "MTIyNjIyNzAwOTI1NzIxNDA3Ng.GvdOMV.2zimM8Sv0skJiZyKbjZJp8QH7YhwAWp4L63z_M"
    val client = DiscordClientBuilder.create(botToken).build().login().block()

    if (client != null) {
        client.eventDispatcher.on(ReadyEvent::class.java).subscribe { event -> run {
            val self = event.self
            println("Logged in as $self")
            }
        }

        client.eventDispatcher.on(MessageCreateEvent::class.java)
                .map(MessageCreateEvent::getMessage)
                .filter { message -> message.author.map { user -> !user.isBot }.orElse(false) }
                .filter { message -> message.content.contains("@1226227009257214076", ignoreCase = true) }
                .filter { message -> message.content.contains("kategorie", ignoreCase = true) }
                .flatMap(Message::getChannel)
                .flatMap { channel -> channel.createMessage("**Kategorie:**\n" +
                        "- Karciane\n" +
                        "- Strategiczne\n" +
                        "- Towarzyskie") }
                .subscribe()

        client.eventDispatcher.on(MessageCreateEvent::class.java)
                .map(MessageCreateEvent::getMessage)
                .filter { message -> message.author.map { user -> !user.isBot }.orElse(false) }
                .filter { message -> message.content.contains("@1226227009257214076", ignoreCase = true) }
                .filter { message -> message.content.contains("karciane", ignoreCase = true) }
                .flatMap(Message::getChannel)
                .flatMap { channel -> channel.createMessage("**Karciane:**\n" +
                        "- Poker\n" +
                        "- Munchkin\n" +
                        "- Załoga") }
                .subscribe()

        client.eventDispatcher.on(MessageCreateEvent::class.java)
                .map(MessageCreateEvent::getMessage)
                .filter { message -> message.author.map { user -> !user.isBot }.orElse(false) }
                .filter { message -> message.content.contains("@1226227009257214076", ignoreCase = true) }
                .filter { message -> message.content.contains("strategiczne", ignoreCase = true) }
                .flatMap(Message::getChannel)
                .flatMap { channel -> channel.createMessage("**Strategiczne:**\n" +
                        "- Twilight Imperium II\n" +
                        "- Twilight Imperium IV\n" +
                        "- Twilight Imperium III") }
                .subscribe()

        client.eventDispatcher.on(MessageCreateEvent::class.java)
                .map(MessageCreateEvent::getMessage)
                .filter { message -> message.author.map { user -> !user.isBot }.orElse(false) }
                .filter { message -> message.content.contains("@1226227009257214076", ignoreCase = true) }
                .filter { message -> message.content.contains("towarzyskie", ignoreCase = true) }
                .flatMap(Message::getChannel)
                .flatMap { channel -> channel.createMessage("**Towarzyskie:**\n" +
                        "- Tajniacy\n" +
                        "- Taboo\n" +
                        "- Mamy szpiega") }
                .subscribe()

        client.onDisconnect().block()
    }
}

