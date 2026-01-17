const { createDefaultPreset } = require("ts-jest");

const tsJestTransformCfg = createDefaultPreset().transform;

/** @type {import("jest").Config} **/
module.exports = {
  testEnvironment: "node",
  testMatch: ["**/?(*.)+(spec|test).(ts|tsx|js|jsx)"],
  transform: {
    ...tsJestTransformCfg,
  },
};