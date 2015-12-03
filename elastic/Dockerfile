FROM java

ENV ES_PKG_NAME elasticsearch-2.0.0

# Install Elasticsearch.
RUN \
  cd / && \
  wget https://download.elasticsearch.org/elasticsearch/elasticsearch/$ES_PKG_NAME.tar.gz && \
  tar xvzf $ES_PKG_NAME.tar.gz && \
  rm -f $ES_PKG_NAME.tar.gz && \
  mv /$ES_PKG_NAME /elasticsearch

# Install HEAD and HQ plugin.
RUN \
  cd /elasticsearch && \
  bin/plugin install mobz/elasticsearch-head && \
  bin/plugin install royrusso/elasticsearch-HQ

# Adding user.
RUN groupadd -r elasticsearch \
 && useradd -r -g elasticsearch elasticsearch
RUN chown -R elasticsearch:elasticsearch /elasticsearch

# TODO enable those properties when you have bigger size machines
# Heap size defaults to 256m min, 1g max
# Set ES_HEAP_SIZE to 50% of available RAM, but no more than 31g
#ENV ES_HEAP_SIZE=2g

# Additional Java OPTS
#ENV ES_JAVA_OPTS="-Xmx2g -Xms2g"

# Define mountable directories.
VOLUME ["/data"]

# Mount elasticsearch.yml config.
ADD elasticsearch.yml /elasticsearch/config/elasticsearch.yml

# Define working directory.
WORKDIR /data

# Define default command.
USER elasticsearch
CMD ["/elasticsearch/bin/elasticsearch"]

# Expose ports.
#   - 9200: HTTP
#   - 9300: transport
EXPOSE 9200 9300