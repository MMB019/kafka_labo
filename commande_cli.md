# Commandes de base Kafka CLI

## Gestion des Topics

### Créer un topic
```bash
kafka-topics.sh --create --topic mon-topic \
  --bootstrap-server localhost:9092 \
  --partitions 3 \
  --replication-factor 2
```

### Lister les topics
```bash
kafka-topics.sh --list --bootstrap-server localhost:9092
```

### Décrire un topic
```bash
kafka-topics.sh --describe --topic mon-topic --bootstrap-server localhost:9092
```

### Modifier un topic (augmenter le nombre de partitions)
```bash
kafka-topics.sh --alter --topic mon-topic \
  --bootstrap-server localhost:9092 \
  --partitions 5
```

### Supprimer un topic
```bash
kafka-topics.sh --delete --topic mon-topic --bootstrap-server localhost:9092
```

## Production de messages

### Producteur en ligne de commande
```bash
kafka-console-producer.sh --broker-list localhost:9092 --topic mon-topic
```

### Producteur avec clés
```bash
kafka-console-producer.sh --broker-list localhost:9092 \
  --topic mon-topic \
  --property "parse.key=true" \
  --property "key.separator=:"
```

### Producteur avec un fichier de propriétés
```bash
kafka-console-producer.sh --broker-list localhost:9092 \
  --topic mon-topic \
  --producer.config producer.properties
```

## Consommation de messages

### Consommateur basique
```bash
kafka-console-consumer.sh --bootstrap-server localhost:9092 \
  --topic mon-topic
```

### Consommateur depuis le début
```bash
kafka-console-consumer.sh --bootstrap-server localhost:9092 \
  --topic mon-topic \
  --from-beginning
```

### Consommateur avec affichage des clés
```bash
kafka-console-consumer.sh --bootstrap-server localhost:9092 \
  --topic mon-topic \
  --property "print.key=true" \
  --property "key.separator=:"
```

### Consommateur avec un groupe de consommateurs
```bash
kafka-console-consumer.sh --bootstrap-server localhost:9092 \
  --topic mon-topic \
  --group mon-groupe-consommateurs
```

### Consommateur avec formatage (timestamp)
```bash
kafka-console-consumer.sh --bootstrap-server localhost:9092 \
  --topic mon-topic \
  --formatter kafka.tools.DefaultMessageFormatter \
  --property print.timestamp=true \
  --property print.key=true \
  --property print.value=true
```

## Gestion des groupes de consommateurs

### Lister les groupes
```bash
kafka-consumer-groups.sh --bootstrap-server localhost:9092 --list
```

### Décrire un groupe (voir les offsets)
```bash
kafka-consumer-groups.sh --bootstrap-server localhost:9092 \
  --describe --group mon-groupe-consommateurs
```

### Réinitialiser les offsets d'un groupe
```bash
kafka-consumer-groups.sh --bootstrap-server localhost:9092 \
  --group mon-groupe-consommateurs \
  --reset-offsets --to-earliest --execute --topic mon-topic
```

## Outils d'administration

### Vérifier les configurations du broker
```bash
kafka-configs.sh --bootstrap-server localhost:9092 \
  --entity-type brokers --entity-name 0 --describe
```

### Modifier la configuration d'un topic
```bash
kafka-configs.sh --bootstrap-server localhost:9092 \
  --entity-type topics --entity-name mon-topic \
  --alter --add-config retention.ms=86400000
```

### Tester la performance du producteur
```bash
kafka-producer-perf-test.sh --topic mon-topic \
  --num-records 1000000 \
  --record-size 1000 \
  --throughput 100000 \
  --producer-props bootstrap.servers=localhost:9092
```

### Tester la performance du consommateur
```bash
kafka-consumer-perf-test.sh --bootstrap-server localhost:9092 \
  --topic mon-topic --messages 1000000
```

## Outils de maintenance

### Vérifier les réplications en retard
```bash
kafka-replica-verification.sh --broker-list localhost:9092 \
  --topic-white-list mon-topic
```

### Récupérer les IDs des partitions leaders
```bash
kafka-topics.sh --describe --bootstrap-server localhost:9092 \
  --topic mon-topic | grep Leader
```

### Dump des logs
```bash
kafka-dump-log.sh --files /tmp/kafka-logs/mon-topic-0/00000000000000000000.log
```

## Commandes Zookeeper (pour versions antérieures à KRaft)

### Connecter au client Zookeeper
```bash
zookeeper-shell.sh localhost:2181
```

### Lister les brokers depuis Zookeeper
```bash
zookeeper-shell.sh localhost:2181 ls /brokers/ids
```

### Obtenir des informations sur un broker
```bash
zookeeper-shell.sh localhost:2181 get /brokers/ids/0
```

## TP supplémentaire - Exercices CLI

### Exercice 1: Création et manipulation de topics
1. Créer un topic nommé "transactions" avec 4 partitions et un facteur de réplication de 2
2. Lister tous les topics pour vérifier sa création
3. Décrire le topic "transactions" pour voir sa configuration
4. Augmenter le nombre de partitions à 6
5. Vérifier que le changement a été effectué

### Exercice 2: Production et consommation de messages
1. Produire 10 messages dans le topic "transactions" avec des clés
2. Consommer les messages depuis le début avec affichage des clés
3. Créer un groupe de consommateurs et consommer les messages
4. Vérifier les offsets du groupe
5. Réinitialiser les offsets et consommer à nouveau

### Exercice 3: Configuration et monitoring
1. Modifier la configuration du topic "transactions" pour réduire le temps de rétention à 1 heure
2. Vérifier que la configuration a bien été appliquée
3. Exécuter un test de performance de production
4. Surveiller les métriques pendant le test