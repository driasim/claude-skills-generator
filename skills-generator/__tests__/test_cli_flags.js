import { describe, it, expect } from 'vitest';
import { execSync } from 'child_process';

const CLI = 'node bin/skill.js';

describe('CLI Enhance Flags', () => {
  it('should accept --output-dir flag', () => {
    const { stdout } = execSync(`${CLI} --help`, { encoding: 'utf8' });
    expect(stdout).toContain('--output-dir');
  });

  it('should accept --template / -t flag', () => {
    const { stdout } = execSync(`${CLI} --help`, { encoding: 'utf8' });
    expect(stdout).toContain('--template');
  });

  it('should accept --verbose / -v flag', () => {
    const { stdout } = execSync(`${CLI} --help`, { encoding: 'utf8' });
    expect(stdout).toContain('--verbose');
  });

  it('should accept --dry-run / -n flag', () => {
    const { stdout } = execSync(`${CLI} --help`, { encoding: 'utf8' });
    expect(stdout).toContain('--dry-run');
  });

  it('should accept --format flag (json/markdown)', () => {
    const { stdout } = execSync(`${CLI} --help`, { encoding: 'utf8' });
    expect(stdout).toContain('--format');
  });

  it('should accept --config / -c flag', () => {
    const { stdout } = execSync(`${CLI} --help`, { encoding: 'utf8' });
    expect(stdout).toContain('--config');
  });

  it('should accept --force flag', () => {
    const { stdout } = execSync(`${CLI} --help`, { encoding: 'utf8' });
    expect(stdout).toContain('--force');
  });

  it('should accept --yes / -y flag', () => {
    const { stdout } = execSync(`${CLI} --help`, { encoding: 'utf8' });
    expect(stdout).toContain('--yes');
  });
});
