FROM node:latest as builder

RUN mkdir /usr/src/app

WORKDIR /usr/src/app

ENV PATH /usr/src/app/node_modules/.bin:$PATH

COPY package.json /usr/src/app/package.json

RUN npm install -g npm@9.6.5
RUN npm install 
RUN npm install react-scripts@3.4.1 -g

COPY . /usr/src/app

RUN npm run build

FROM nginx

# RUN rm -rf /etc/nginx/conf.d

# COPY conf /etc/nginx

# COPY --from=builder /usr/src/app/build /usr/share/nginx/html

COPY --from=builder /usr/src/app/dist /app

COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 3100

CMD ["nginx", "-g", "daemon off;"]