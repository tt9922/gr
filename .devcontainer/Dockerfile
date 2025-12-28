FROM library/python:3.11.9-bookworm

# 3.11のまま(3.11.11)だとPyinstallerで生成した実行ファイルが
# Windows11のubuntu(Python:3.10.12)の環境で実行エラーが
# でるようになっため、3.11.9に固定。20250120

ARG USER=vscode
ARG DEBIAN_FRONTEND=noninteractive

# --- Environment Variables ---
ENV PATH="/home/vscode/.local/bin:${PATH}" \
    LANG=ja_JP.UTF-8 \
    LANGUAGE=ja_JP:ja \
    LC_ALL=ja_JP.UTF-8 \
    TZ=JST-9 \
    TERM=xterm

# --- System Dependencies & Setup ---
RUN apt-get update && apt-get install -y --no-install-recommends \
    # Essential Tools
    build-essential \
    ca-certificates \
    clang \
    cmake \
    locales \
    ninja-build \
    sudo \
    wget \
    # GStreamer & Media Dependencies
    gstreamer1.0-alsa \
    gstreamer1.0-gl \
    gstreamer1.0-gtk3 \
    gstreamer1.0-libav \
    gstreamer1.0-plugins-bad \
    gstreamer1.0-plugins-base \
    gstreamer1.0-plugins-good \
    gstreamer1.0-plugins-ugly \
    gstreamer1.0-pulseaudio \
    gstreamer1.0-qt5 \
    gstreamer1.0-tools \
    gstreamer1.0-x \
    libgstreamer-plugins-bad1.0-dev \
    libgstreamer-plugins-base1.0-dev \
    libgstreamer1.0-dev \
    libgtk-3-dev \
    libmpv-dev \
    mpv \
    ffmpeg \
    # Development Libraries
    libffi-dev \
    libgdbm-dev \
    liblzma-dev \
    libncurses5-dev \
    libnss3-dev \
    libssl-dev \
    libreadline-dev \
    libstdc++-12-dev \
    libsystemd0 \
    libvshadow-utils \
    zlib1g-dev \
    # Fonts & Desktop Utilities
    desktop-file-utils \
    fonts-ipafont \
    fonts-noto-cjk \
    xdg-utils \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    # User Setup
    && useradd -m -s /usr/bin/bash ${USER} \
    && echo "${USER} ALL=(ALL) NOPASSWD: ALL" >/etc/sudoers.d/${USER} \
    && chmod 0440 /etc/sudoers.d/${USER} \
    && gpasswd -a ${USER} sudo \
    # Locale Generation
    && sed -i '/ja_JP.UTF-8/s/^# //g' /etc/locale.gen \
    && locale-gen \
    && locale-gen ja_JP.UTF-8 \
    && localedef -i ja_JP -c -f UTF-8 -A /usr/share/locale/locale.alias ja_JP.UTF-8

# --- Python Package Installation ---
# Note: yt-dlp is pinned to a specific dev version as per original requirements.
RUN pip install --no-cache-dir --upgrade pip setuptools cython \
    && pip install --no-cache-dir \
    "flet[all]" \
    beautifulsoup4 \
    DateTime \
    googletrans \
    requests \
    urllib3 \
    yt-dlp==2025.11.15.232912.dev0
