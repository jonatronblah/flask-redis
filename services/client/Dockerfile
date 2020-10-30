FROM node:15.0.1-buster-slim

WORKDIR /usr/src/app

COPY  package*.json ./

RUN npm install

COPY . /usr/src/app/



CMD ["npm", "start"]
