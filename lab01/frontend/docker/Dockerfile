# build stage
FROM node:lts-alpine as build-stage
WORKDIR /src
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# production stage
FROM nginx:stable-alpine as production-stage
COPY nginx/config/nginx.conf /etc/nginx/nginx.conf
COPY nginx/config/default.conf /etc/nginx/conf.d/default.conf
COPY --from=build-stage /src/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]