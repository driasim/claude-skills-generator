#!/usr/bin/env node

import yargs from "yargs";
import { hideBin } from "yargs/helpers";

const argv = yargs(hideBin(process.argv))
  .option('skip-validation', { type: 'boolean', description: 'Skip validation checks' })
  .parse();

console.log("CLI ready");
